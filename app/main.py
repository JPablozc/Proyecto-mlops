# app/main.py
"""
API REST para predicción de niveles de obesidad.
Ejecutar con: uvicorn app.main:app --reload
"""
from fastapi import FastAPI
import joblib
import pandas as pd
from src.config import MODEL_PATH

# 👇 ESTA variable es la que uvicorn necesita
app = FastAPI(title="Obesity Prediction API")

# Carga del modelo
bundle = joblib.load(MODEL_PATH)
model, le = bundle["model"], bundle["label_encoder"]

@app.get("/")
def home():
    """Endpoint de prueba para verificar que la API funciona."""
    return {"message": "API de predicción de niveles de obesidad lista."}

@app.post("/predict")
def predict(data: dict):
    """Recibe un diccionario con los datos del usuario y devuelve la clase predicha."""
    X = pd.DataFrame([data])
    pred = le.inverse_transform(model.predict(X))[0]
    return {"prediction": pred}
