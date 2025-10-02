# tests/test_train.py
import joblib
import pandas as pd
from src.config import MODEL_PATH, PROCESSED_CSV

def test_model_file_exists():
    assert MODEL_PATH.exists()

def test_model_predict_shape():
    bundle = joblib.load(MODEL_PATH)
    model, le = bundle["model"], bundle["label_encoder"]
    df = pd.read_csv(PROCESSED_CSV)
    X = df.drop(columns=["target"])
    preds = le.inverse_transform(model.predict(X))
    assert len(preds) == len(X)
