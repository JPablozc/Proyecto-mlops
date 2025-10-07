# Proyecto: Predicción de Niveles de Obesidad
### Por: Juan Pablo Zapata Chavarriaga
### Universidad de Medellín

---

## 1. Contexto y Motivación
La obesidad es un problema de salud pública a nivel mundial, asociado con enfermedades crónicas como diabetes tipo 2, hipertensión y enfermedades cardiovasculares.  
Identificar tempranamente factores de riesgo a partir de hábitos alimenticios y actividad física puede ayudar a diseñar programas de prevención y políticas de salud más efectivas.

Este proyecto busca desarrollar un **MVP (Minimum Viable Product)** que permita predecir el nivel de obesidad de una persona a partir de sus hábitos de vida, implementando un flujo completo de **Machine Learning y MLOps**, que abarque desde la preparación de datos hasta el despliegue del modelo en producción.

---

## 2. Dataset
El dataset utilizado proviene de [UCI Machine Learning Repository – Estimation of obesity levels](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition).  
Contiene **2,111 registros** con **17 variables** que describen características demográficas, hábitos alimenticios y niveles de actividad física.

### Tabla de variables

| Variable | Tipo | Descripción |
|-----------|------|-------------|
| Gender | Categórica | Género de la persona (Hombre/Mujer). |
| Age | Numérica | Edad en años (14–61). |
| Height | Numérica | Altura en metros (1.45–1.98). |
| Weight | Numérica | Peso en kilogramos (39–173). |
| family_history_with_overweight | Categórica | Antecedentes familiares de sobrepeso. |
| FAVC | Categórica | Consumo frecuente de comida rápida (sí/no). |
| FCVC | Ordinal | Frecuencia de consumo de vegetales (1–3). |
| NCP | Ordinal | Número de comidas principales al día (1–4). |
| CAEC | Categórica | Consumo de alimentos entre comidas. |
| SMOKE | Categórica | Hábito de fumar. |
| CH2O | Ordinal | Consumo de agua diario en litros (1–3). |
| SCC | Categórica | Calorías consumidas entre comidas controladas (sí/no). |
| FAF | Ordinal | Frecuencia de actividad física semanal (0–3). |
| TUE | Ordinal | Tiempo usando dispositivos electrónicos (0–2). |
| CALC | Categórica | Consumo de alcohol. |
| MTRANS | Categórica | Medio de transporte principal. |
| NObeyesdad | Categórica (target) | Nivel de obesidad (7 categorías: Insufficient_Weight, Normal_Weight, Overweight I/II, Obesity I/II/III). |

---

## 3. Objetivo del Proyecto
Construir un modelo de machine learning que, a partir de las variables de hábitos alimenticios y estilo de vida, **clasifique a los individuos en uno de los siete niveles de obesidad** definidos en el dataset.  
El desarrollo se enmarca en un enfoque **MLOps**, buscando garantizar reproducibilidad, automatización y despliegue eficiente.

---

## 4. Metodología y Flujo de Trabajo

### 4.1. Etapas principales
1. **Análisis Exploratorio (EDA):** revisión estadística y visual de las variables, correlaciones y patrones.
2. **Preprocesamiento:** limpieza de datos, codificación de variables, manejo de tipos, creación del índice de masa corporal (BMI).
3. **Feature Engineering:** generación y selección de nuevas variables predictoras.
4. **Entrenamiento:** comparación de modelos Random Forest y XGBoost mediante búsqueda de hiperparámetros.
5. **Evaluación:** cálculo de métricas (accuracy, F1-score macro) y generación de la matriz de confusión.
6. **Serialización:** guardado del modelo final y pipeline en formato .joblib.
7. **Registro y Orquestación:** automatización del flujo con Prefect y registro de resultados con MLflow.
8. **Despliegue:** implementación de una API con FastAPI para predicciones en tiempo real.

---

## 5. Descripción General del Proyecto
El proyecto implementa un flujo MLOps modular y reproducible, estructurado en directorios para datos, modelos, scripts, API, pruebas y reportes.  
Cada módulo del pipeline (data, features, models) tiene scripts independientes que permiten ejecutar, depurar o actualizar partes del flujo sin afectar el resto del sistema.  
Además, se incluye integración con MLflow y Prefect para el seguimiento de experimentos y la orquestación de tareas, junto con una API lista para desplegar el modelo en un entorno de producción local o en la nube.

---

## 6. Instalación y Ejecución

### 6.1. Configuración del entorno

# Clonar el repositorio
git clone https://github.com/JPablozc/Proyecto-mlops.git
cd Proyecto-mlops

# Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

---

### 6.2. Eje el pipelcutarine completo

python run_pipeline.py

Ejecuta las etapas de descarga, limpieza, feature engineering, entrenamiento, evaluación y registro del modelo.

---

## 7. Monitoreo y Orquestación

### 7.1. MLflow

Visualiza resultados y métricas del entrenamiento:

python -m mlflow ui

Acceder desde: http://127.0.0.1:5000

---

### 7.2. Prefect

Para ver el flujo automatizado del pipeline:

python src/pipeline_flow.py

Dashboard: http://127.0.0.1:4200

---

## 8. Pruebas Unitarias y CI/CD

Ejecución local de tests:

$env:PYTHONPATH="."; pytest -q

El proyecto incluye un flujo de GitHub Actions que ejecuta pruebas automáticas al hacer push.

---

## 9. Despliegue del Modelo (API)

API REST creada con FastAPI.

Ejecutar el servidor:

uvicorn app.main:app --reload

Interfaz Swagger: http://127.0.0.1:8000/docs

Ejemplo de entrada:
{
  "Gender": "Male",
  "Age": 25,
  "Height": 1.75,
  "Weight": 80,
  "family_history_with_overweight": "yes",
  "FAVC": "yes",
  "FCVC": 2,
  "NCP": 3,
  "CAEC": "Sometimes",
  "SMOKE": "no",
  "CH2O": 2,
  "SCC": "no",
  "FAF": 1,
  "TUE": 1,
  "CALC": "Sometimes",
  "MTRANS": "Automobile",
  "BMI": 26.1
}

Salida esperada:
{"prediction": "Overweight_Level_I"}

---
## 10. Conclusiones

- Se desarrolló un flujo MLOps completo, desde el preprocesamiento hasta el despliegue.
- El modelo XGBoost obtuvo un rendimiento superior al 95% de precisión.
- El proyecto es completamente reproducible, automatizado y trazable.
