# src/config.py
"""
Configuraciones centrales del proyecto:
- rutas de datos, modelos y reportes
- parámetros de entrenamiento
"""

from pathlib import Path

# Rutas base
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Archivos
RAW_CSV = RAW_DIR / "obesity.csv"
PROCESSED_CSV = PROCESSED_DIR / "dataset.csv"
MODEL_PATH = MODELS_DIR / "best_model.joblib"
METRICS_JSON = REPORTS_DIR / "metrics.json"
CONF_MATRIX_PNG = REPORTS_DIR / "confusion_matrix.png"

# ML
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_JOBS = -1
