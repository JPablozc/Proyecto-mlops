# src/data/download_data.py
"""
Ingesta de datos.
Aquí simplemente leemos el CSV ya guardado en data/raw/obesity.csv.
"""
import pandas as pd
from src.config import RAW_CSV
from src.utils import ensure_dirs

def main() -> None:
    ensure_dirs(RAW_CSV.parent)
    df = pd.read_csv(RAW_CSV)
    print(f"✅ Datos encontrados en {RAW_CSV} con forma {df.shape}")
    print(f"📊 Columnas: {list(df.columns)}")

if __name__ == "__main__":
    main()
