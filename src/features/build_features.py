# src/features/build_features.py
"""
Ingeniería de features:
- Crea BMI = Weight / Height^2
"""
import pandas as pd
from src.config import PROCESSED_CSV

def main() -> None:
    df = pd.read_csv(PROCESSED_CSV)

    if "Weight" in df.columns and "Height" in df.columns:
        df["BMI"] = df["Weight"] / (df["Height"] ** 2)

    df.to_csv(PROCESSED_CSV, index=False)
    print(f"Features construidas y guardadas en {PROCESSED_CSV}; columnas: {list(df.columns)}")

if __name__ == "__main__":
    main()
