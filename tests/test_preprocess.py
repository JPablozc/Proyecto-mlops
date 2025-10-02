# tests/test_preprocess.py
import pandas as pd
from src.config import PROCESSED_CSV
from pathlib import Path

def test_processed_file_exists():
    assert Path(PROCESSED_CSV).exists()

def test_no_nulls_and_has_target():
    df = pd.read_csv(PROCESSED_CSV)
    assert "target" in df.columns
    assert not df.isnull().any().any()
