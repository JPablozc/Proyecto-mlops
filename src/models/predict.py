# src/models/predict.py
"""
Script de predicción por lote.
"""
import argparse
import joblib
import pandas as pd
from src.config import MODEL_PATH

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV de entrada sin 'target'")
    parser.add_argument("--output", required=True, help="CSV de salida con predicciones")
    args = parser.parse_args()

    bundle = joblib.load(MODEL_PATH)
    model, le = bundle["model"], bundle["label_encoder"]

    X = pd.read_csv(args.input)
    preds_enc = model.predict(X)
    preds_lbl = le.inverse_transform(preds_enc)

    out = X.copy()
    out["prediction"] = preds_lbl
    out.to_csv(args.output, index=False)
    print(f" Predicciones guardadas en {args.output}")

if __name__ == "__main__":
    main()
