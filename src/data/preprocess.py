# src/data/preprocess.py
"""
Preprocesamiento de datos:
- Renombrar columna objetivo a 'target'
- Eliminar duplicados y nulos
- Guardar dataset limpio en CSV
"""
import pandas as pd
from src.config import RAW_CSV, PROCESSED_CSV, PROCESSED_DIR
from src.utils import ensure_dirs

RENAME_MAP = {
    "NObeyesdad": "target",
    "NObesity": "target",
    "NObese": "target",
    "CH20": "CH2O"
}

def main() -> None:
    ensure_dirs(PROCESSED_DIR)
    df = pd.read_csv(RAW_CSV)

    # Renombrar columnas
    df = df.rename(columns={c: RENAME_MAP.get(c, c) for c in df.columns})

    if "target" not in df.columns:
        raise ValueError("No se encontró la columna objetivo en el dataset.")

    # Limpieza
    df = df.drop_duplicates().dropna().reset_index(drop=True)

    # Guardar en CSV
    df.to_csv(PROCESSED_CSV, index=False)
    print(f"✅ Preprocesado guardado en {PROCESSED_CSV} con forma {df.shape}")

if __name__ == "__main__":
    main()
