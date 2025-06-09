# Brain Tumor MRI Dataset

## Descripción
Este conjunto de datos contiene 7023 imágenes de resonancia magnética (MRI) de cerebros humanos clasificadas en cuatro categorías: glioma, meningioma, tumor pituitario y sin tumor. Cada imagen corresponde a un corte de MRI, etiquetado según la presencia y el tipo de tumor cerebral.

## Estructura del dataset
- La carpeta principal se divide en cuatro subcarpetas, una por cada clase:
  - **glioma_tumor/**: imágenes con diagnóstico de glioma.
  - **meningioma_tumor/**: imágenes con diagnóstico de meningioma.
  - **pituitary_tumor/**: imágenes con diagnóstico de tumor pituitario.
  - **no_tumor/**: imágenes de cerebros sin presencia de tumor.
- Dentro de cada subcarpeta, las imágenes están en formato JPEG (.jpg).

## Clases
1. **Glioma**  
2. **Meningioma**  
3. **Pituitary (tumor pituitario)**  
4. **No Tumor**  

## Formato y contenido
- **Número total de imágenes:** 7023  
- **Resolución aproximada:** variable, pero la mayoría alrededor de 512×512 píxeles.  
- **Formato de archivo:** JPEG (.jpg).
- **Etiquetado:** cada imagen se nombra con un identificador único, sin incluir la etiqueta en el nombre de archivo; la etiqueta se deduce de la carpeta en la que se encuentra.

## Uso
1. Descargar y descomprimir el archivo principal provisto por Kaggle.  
2. Confirmar que la estructura de carpetas sea:
   - `brain_tumor_dataset/glioma_tumor/`
   - `brain_tumor_dataset/meningioma_tumor/`
   - `brain_tumor_dataset/pituitary_tumor/`
   - `brain_tumor_dataset/no_tumor/`  


## Licencia
El dataset está disponible bajo la licencia proporcionada por Kaggle. Se debe consultar la sección de “Licencia” en la página oficial del conjunto de datos para detalles específicos.


## ¿Qué es un glioma?
Un **glioma** es un tipo de neoplasia que se origina en las células gliales del sistema nervioso central, ya sea en el cerebro o en la médula espinal. Se le llama así porque surge de las células de soporte (glía) y su ubicación más frecuente es el cerebro.  
- **Clasificación por tipo de célula:**  
  - Ependimomas (células ependimarias)  
  - Astrocitomas (astrocitos), siendo el glioblastoma multiforme el más común y agresivo  
  - Oligodendrogliomas (oligodendrocitos)  
- **Por grado (según la OMS):**  
  - Grado I: tumores de bajo grado (bien diferenciados, generalmente benignos).  
  - Grado II: tumores de bajo grado pero con comportamiento más invasivo.  
  - Grado III: tumores anaplásicos (alto grado, malignos).  
  - Grado IV: glioblastoma multiforme (el más agresivo).  
- **Síntomas:** pueden incluir dolores de cabeza, náuseas, vómitos, convulsiones y déficits neurológicos debido al aumento de la presión intracraneal o a la afectación de áreas específicas del cerebro. citeturn2search7

## ¿Qué es un meningioma?
Un **meningioma** es un tumor encefálico que se desarrolla en el tejido aracnoideo de las meninges, la membrana que recubre el cerebro y la médula espinal, y suele adherirse a la duramadre. Generalmente es benigno y de crecimiento lento, aunque puede llegar a ser atípico o anaplásico en pocos casos.  
- **Frecuencia:** representa entre el 13 % y el 26 % de los tumores intracraneales primarios en adultos.  
- **Distribución por sexo y edad:** aparece más frecuentemente en mujeres (relación aproximada 3:2) y es más común entre la sexta y la séptima décadas de la vida, aunque puede ocurrir en cualquier edad.  
- **Síntomas:** a menudo se descubren de manera incidental sin síntomas; cuando los hay, dependen de la localización e incluyen cefaleas, convulsiones, alteraciones visuales y déficits neurológicos focales, producto de la compresión del tejido cerebral adyacente.  
- **Clasificación OMS:**  
  - Grado I (benigno)  
  - Grado II (atípico)  
  - Grado III (anaplásico, maligno) citeturn3search0

## ¿Qué es un tumor pituitario?
Un **tumor pituitario** (o adenoma hipofisario) es una proliferación anómala de células en la glándula pituitaria (hipófisis), ubicada en la base del cráneo y responsable de la producción de hormonas que regulan otras glándulas endocrinas.  
- **Naturaleza:** la mayoría son adenomas benignos. Solo entre el 0,1 % y el 0,2 % son tumores malignos (carcinomas de hipófisis).  
- **Clasificación:**  
  - **Funcionantes:** secretan hormonas (por ejemplo, prolactina, hormona del crecimiento, ACTH), pudiendo causar síndromes endocrinos como acromegalia o enfermedad de Cushing.  
  - **No funcionantes:** no secretan hormonas, pero pueden causar síntomas por compresión local (cefaleas, alteraciones visuales).  
- **Prevalencia:** representan entre el 10 % y el 25 % de todas las neoplasias intracraneales, con una prevalencia estimada cercana al 17 % de la población general (muchos se detectan incidentalmente en estudios de imagen).  
- **Síntomas:** dependen de si secretan hormonas o no. Los funcionantes generan desequilibrios hormonales; los no funcionantes, síntomas por efecto masa (cefaleas, alteración del campo visual). 
