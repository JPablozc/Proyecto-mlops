# run_pipeline.py
"""
Pipeline completo de pasos: ingestión -> preprocesamiento -> features -> entrenamiento -> evaluación
"""
import subprocess, sys

STEPS = [
    "python -m src.data.download_data",
    "python -m src.data.preprocess",
    "python -m src.features.build_features",
    "python -m src.models.train_model",
    "python -m src.models.evaluate",
]

def run(cmd: str):
    print(f"\n$ {cmd}")
    ret = subprocess.run(cmd, shell=True)
    if ret.returncode != 0:
        sys.exit(ret.returncode)

if __name__ == "__main__":
    for step in STEPS:
        run(step)
    print("\n Pipeline completo OK")
