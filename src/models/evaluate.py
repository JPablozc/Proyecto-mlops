# src/models/evaluate.py
"""
Evalúa el modelo guardado y genera matriz de confusión en reports/.
"""
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from src.config import PROCESSED_CSV, MODEL_PATH, CONF_MATRIX_PNG, REPORTS_DIR
from src.utils import ensure_dirs

def main():
    ensure_dirs(REPORTS_DIR)
    bundle = joblib.load(MODEL_PATH)
    model = bundle["model"]
    le = bundle["label_encoder"]

    df = pd.read_csv(PROCESSED_CSV)
    X, y_true = df.drop(columns=["target"]), df["target"]

    y_pred_enc = model.predict(X)
    y_pred = le.inverse_transform(y_pred_enc)

    labels = sorted(y_true.unique().tolist())
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(cm, display_labels=labels)

    fig, ax = plt.subplots(figsize=(10, 8))
    disp.plot(ax=ax, xticks_rotation=45, colorbar=False)
    plt.tight_layout()
    fig.savefig(CONF_MATRIX_PNG, dpi=150)
    print(f"🖼️ Matriz de confusión guardada en {CONF_MATRIX_PNG}")

if __name__ == "__main__":
    main()
