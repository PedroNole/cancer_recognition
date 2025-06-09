import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('lgbm.pkl', 'rb') as f:
    model = pickle.load(f)
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

st.title('Predicción de Cáncer de Apéndice')

def options_from_encoder(col):
    return encoders[col].classes_ if col in encoders else ['None']

with st.form("form_prediccion"):
    country         = st.selectbox("Country", options_from_encoder('Country'))
    age             = st.number_input("Age", 0, 120, 40)
    gender          = st.selectbox("Gender", options_from_encoder('Gender'))
    bmi             = st.number_input("BMI", 10.0, 60.0, 25.0)
    smoking_status  = st.selectbox("Smoking Status", options_from_encoder('Smoking_Status'))
    alcohol         = st.selectbox("Alcohol Consumption", options_from_encoder('Alcohol_Consumption'))
    family_history  = st.selectbox("Family History Cancer", options_from_encoder('Family_History_Cancer'))
    genetic_mut     = st.selectbox("Genetic Mutations", options_from_encoder('Genetic_Mutations'))
    chronic_dis     = st.selectbox("Chronic Diseases", options_from_encoder('Chronic_Diseases'))
    activity        = st.selectbox("Physical Activity Level", options_from_encoder('Physical_Activity_Level'))
    diet_type       = st.selectbox("Diet Type", options_from_encoder('Diet_Type'))
    radiation       = st.selectbox("Radiation Exposure", options_from_encoder('Radiation_Exposure'))
    prev_cancer     = st.selectbox("Previous Cancers", options_from_encoder('Previous_Cancers'))
    blood_pressure  = st.number_input("Blood Pressure", 60.0, 200.0, 120.0)
    chol            = st.number_input("Cholesterol Level", 100.0, 400.0, 200.0)
    wbc             = st.number_input("White Blood Cell Count", 1.0, 20.0, 7.0)
    rbc             = st.number_input("Red Blood Cell Count", 2.0, 8.0, 5.0)
    platelets       = st.number_input("Platelet Count", 50.0, 500.0, 250.0)
    tumor_markers   = st.selectbox("Tumor Markers", options_from_encoder('Tumor_Markers'))
    symptom_sev     = st.selectbox("Symptom Severity", options_from_encoder('Symptom_Severity'))
    diag_delay      = st.number_input("Diagnosis Delay Days", 0, 1000, 0)
    treatment_type  = st.selectbox("Treatment Type", options_from_encoder('Treatment_Type'))
    survival_years  = st.number_input("Survival Years After Diagnosis", 0.0, 20.0, 0.0)

    submit = st.form_submit_button("Predecir")

if submit:
    X_new = pd.DataFrame([{
        'Country': country,
        'Age': age,
        'Gender': gender,
        'BMI': bmi,
        'Smoking_Status': smoking_status,
        'Alcohol_Consumption': alcohol,
        'Family_History_Cancer': family_history,
        'Genetic_Mutations': genetic_mut,
        'Chronic_Diseases': chronic_dis,
        'Physical_Activity_Level': activity,
        'Diet_Type': diet_type,
        'Radiation_Exposure': radiation,
        'Previous_Cancers': prev_cancer,
        'Blood_Pressure': blood_pressure,
        'Cholesterol_Level': chol,
        'White_Blood_Cell_Count': wbc,
        'Red_Blood_Cell_Count': rbc,
        'Platelet_Count': platelets,
        'Tumor_Markers': tumor_markers,
        'Symptom_Severity': symptom_sev,
        'Diagnosis_Delay_Days': diag_delay,
        'Treatment_Type': treatment_type,
        'Survival_Years_After_Diagnosis': survival_years
    }])

    for col in encoders:
        if col in X_new:
            X_new[col] = encoders[col].transform(X_new[col])

    y_pred = model.predict(X_new)[0]
    y_proba = model.predict_proba(X_new)[0][1]
    result = "Cáncer" if y_pred == 1 else "No cáncer"
    st.success(f"Predicción: **{result}** (Probabilidad de cáncer: {y_proba:.2%})")
