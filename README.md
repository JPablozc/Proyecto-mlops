# Proyecto: Predicción de Niveles de Obesidad
### Por: Juan Pablo Zapata Chavarriaga
### Universidad de Medellín

---

## 1. Contexto y Motivación
La obesidad es un problema de salud pública a nivel mundial, asociado con enfermedades crónicas como diabetes tipo 2, hipertensión y enfermedades cardiovasculares.  
Identificar tempranamente factores de riesgo a partir de hábitos alimenticios y actividad física puede ayudar a diseñar programas de prevención y políticas de salud.

Este proyecto busca desarrollar un **MVP (Minimum Viable Product)** que permita predecir el nivel de obesidad de una persona a partir de sus hábitos de vida, usando técnicas de ciencia de datos y aprendizaje automático.

---

## 2. Dataset
El dataset utilizado proviene de [UCI Machine Learning Repository – Estimation of obesity levels](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition).  
Contiene **2,111 registros** con **17 variables** que describen características demográficas, hábitos alimenticios y niveles de actividad física.

### Tabla de variables

| Variable       | Tipo        | Descripción |
|----------------|-------------|-------------|
| Gender         | Categórica  | Género de la persona (Hombre/Mujer). |
| Age            | Numérica    | Edad en años (14–61). |
| Height         | Numérica    | Altura en metros (1.45–1.98). |
| Weight         | Numérica    | Peso en kilogramos (39–173). |
| family_history_with_overweight | Categórica | Antecedentes familiares de sobrepeso. |
| FAVC           | Categórica  | Consumo frecuente de comida rápida (sí/no). |
| FCVC           | Ordinal     | Frecuencia de consumo de vegetales (1–3). |
| NCP            | Ordinal     | Número de comidas principales al día (1–4). |
| CAEC           | Categórica  | Consumo de alimentos entre comidas. |
| SMOKE          | Categórica  | Hábito de fumar. |
| CH2O           | Ordinal     | Consumo de agua diario en litros (1–3). |
| SCC            | Categórica  | Calorías consumidas entre comidas controladas (sí/no). |
| FAF            | Ordinal     | Frecuencia de actividad física semanal (0–3). |
| TUE            | Ordinal     | Tiempo usando dispositivos electrónicos (0–2). |
| CALC           | Categórica  | Consumo de alcohol. |
| MTRANS         | Categórica  | Medio de transporte principal. |
| NObeyesdad     | Categórica (target) | Nivel de obesidad (7 categorías: Insufficient_Weight, Normal_Weight, Overweight I/II, Obesity I/II/III). |

---

## 3. Objetivo del Proyecto
Construir un modelo de machine learning que, a partir de las variables de hábitos alimenticios y estilo de vida, **clasifique a los individuos en uno de los 7 niveles de obesidad** definidos en el dataset.

---

## 4. Metodología Propuesta
1. **EDA (Exploratory Data Analysis):**  
   - Análisis descriptivo de las variables.  
   - Identificación de patrones y relaciones entre hábitos y niveles de obesidad.  
   - Detección de valores atípicos y revisión de distribuciones.  
   - **Análisis de correlaciones mixtas:**  
     - Pearson/Spearman para variables numéricas.  
     - Cramér’s V para variables categóricas.  
     - Correlation Ratio y Mutual Information para relaciones mixtas.  
   - **Heatmap extendido** que combina numéricas y categóricas en una sola matriz de correlación.  

2. **Preprocesamiento:**  
   - Codificación de variables categóricas.  
   - Escalado de variables numéricas si es necesario.  
   - Manejo de desbalanceo si se detecta en subgrupos.  

3. **Modelado Predictivo:**  
   - Entrenamiento de modelos de clasificación (Logistic Regression, Random Forest, XGBoost, etc.).  
   - Comparación de métricas (Accuracy, F1-score macro, Matriz de confusión).  

4. **Evaluación y Validación:**  
   - Validación cruzada.  
   - Interpretabilidad de modelos (importancia de variables).  

5. **MVP y despliegue (MLOps):**  
   - Prototipo de API o notebook interactivo para predecir nivel de obesidad.  
   - Contenerización (Docker) y pipeline reproducible.  
   - Automatización del flujo (entrenamiento, evaluación, despliegue).  

---

## 5. Aplicaciones Prácticas
- Herramientas de **prevención en salud pública**.  
- Sistemas de **recomendación personalizada** para mejorar hábitos.  
- **Apoyo clínico** en la identificación temprana de riesgo de obesidad.  
