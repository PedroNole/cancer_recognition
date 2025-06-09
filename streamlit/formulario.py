import streamlit as st
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms


st.title('Predicción de Cáncer de Cabeza (CNN)')
# 1) definición del CNN (misma que la que entrenaste)
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1   = nn.Conv2d(1, 32, 3, padding=1)
        self.bn1     = nn.BatchNorm2d(32)
        self.conv2   = nn.Conv2d(32, 64, 3, padding=1)
        self.bn2     = nn.BatchNorm2d(64)
        self.pool    = nn.MaxPool2d(2,2)
        self.adapt   = nn.AdaptiveAvgPool2d((8,8))
        self.fc1     = nn.Linear(64*8*8, 256)
        self.fc2     = nn.Linear(256, 128)
        self.fc3     = nn.Linear(128, 1)
        self.dropout = nn.Dropout(0.5)
        self.relu    = nn.ReLU()
    def forward(self, x):
        x = self.pool(self.relu(self.bn1(self.conv1(x))))
        x = self.pool(self.relu(self.bn2(self.conv2(x))))
        x = self.adapt(x)
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x.squeeze(1)
# 2) cargar pesos y definir transform
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
cnn_model = CNN().to(device)
cnn_model.load_state_dict(torch.load('reconocimientoCancer.pth', map_location=device))
cnn_model.eval()
transform = transforms.Compose([
    transforms.Resize((256,256)),
    transforms.ToTensor(),
])
# 3) uploader + botón
uploaded = st.file_uploader("Sube una imagen de cabeza (PNG/JPG)", type=['png','jpg','jpeg'])
if uploaded:
    img = Image.open(uploaded).convert('L')
    st.image(img, caption='Original', use_column_width=True)
    if st.button("Predecir cáncer de cabeza"):
        tensor = transform(img).unsqueeze(0).to(device)  # [1,1,256,256]
        with torch.no_grad():
            logits = cnn_model(tensor).view(-1)          # [1]
            prob   = torch.sigmoid(logits).item()
            pred   = prob > 0.5
        res = "Cáncer detectado" if pred else "No cáncer"
        st.success(f"{res} (Probabilidad de Cáncer: {prob:.2%})")