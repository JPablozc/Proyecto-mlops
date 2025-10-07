# src/pipeline_flow.py
"""
Pipeline orquestado con Prefect
Cada paso se ejecuta como una tarea independiente.
"""
from prefect import flow, task
import subprocess

@task
def download_data(): subprocess.run("python -m src.data.download_data", shell=True)
@task
def preprocess(): subprocess.run("python -m src.data.preprocess", shell=True)
@task
def features(): subprocess.run("python -m src.features.build_features", shell=True)
@task
def train(): subprocess.run("python -m src.models.train_model", shell=True)
@task
def evaluate(): subprocess.run("python -m src.models.evaluate", shell=True)

@flow(name="obesity_mlops_pipeline")
def main_flow():
    download_data()
    preprocess()
    features()
    train()
    evaluate()

if __name__ == "__main__":
    main_flow()
