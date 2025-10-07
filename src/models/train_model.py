# src/models/train_model.py
"""
Entrenamiento de modelos con MLflow Tracking
Registra hiperparámetros, métricas y artefactos.
"""
import joblib
import json
import pandas as pd
import numpy as np
from pathlib import Path
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, classification_report

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from src.config import PROCESSED_CSV, MODEL_PATH, METRICS_JSON, RANDOM_STATE, TEST_SIZE, N_JOBS
from src.utils import ensure_dirs


def infer_column_types(df: pd.DataFrame):
    features = df.drop(columns=["target"])
    num_cols = features.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = [c for c in features.columns if c not in num_cols]
    return num_cols, cat_cols


def build_preprocessor(num_cols, cat_cols):
    num_tf = Pipeline([("scaler", StandardScaler())])
    cat_tf = Pipeline([("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])
    return ColumnTransformer([
        ("num", num_tf, num_cols),
        ("cat", cat_tf, cat_cols)
    ])


def main():
    ensure_dirs(Path(MODEL_PATH).parent, Path(METRICS_JSON).parent)

    df = pd.read_csv(PROCESSED_CSV)
    y_str = df["target"]
    X = df.drop(columns=["target"])

    le = LabelEncoder()
    y = le.fit_transform(y_str)

    num_cols, cat_cols = infer_column_types(df)
    preprocessor = build_preprocessor(num_cols, cat_cols)

    rf = RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=N_JOBS)
    xgb = XGBClassifier(
        random_state=RANDOM_STATE, n_estimators=200, learning_rate=0.1,
        max_depth=6, subsample=0.9, colsample_bytree=0.9,
        tree_method="hist", n_jobs=N_JOBS,
        objective="multi:softprob", num_class=len(le.classes_)
    )

    models = {
        "rf": (rf, {"clf__n_estimators": [200, 400]}),
        "xgb": (xgb, {"clf__n_estimators": [200, 400], "clf__max_depth": [4, 6]})
    }

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    mlflow.set_tracking_uri("mlruns")
    mlflow.set_experiment("obesity_prediction")

    best_model, best_metrics = None, None

    for name, (clf, grid) in models.items():
        pipe = Pipeline([("pre", preprocessor), ("clf", clf)])
        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)
        search = GridSearchCV(pipe, grid, cv=cv, scoring="f1_macro", n_jobs=N_JOBS)
        search.fit(X_train, y_train)

        y_pred = search.best_estimator_.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1m = f1_score(y_test, y_pred, average="macro")
        report = classification_report(y_test, y_pred, output_dict=True)

        # === MLflow logging ===
        with mlflow.start_run(run_name=name):
            mlflow.log_params(search.best_params_)
            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("f1_macro", f1m)
            mlflow.sklearn.log_model(search.best_estimator_, "model")
            mlflow.log_dict(report, "classification_report.json")

        if best_metrics is None or f1m > best_metrics["f1_macro"]:
            best_model = search.best_estimator_
            best_metrics = {
                "model": name,
                "best_params": search.best_params_,
                "accuracy": round(acc, 4),
                "f1_macro": round(f1m, 4),
                "report": report,
                "classes": le.classes_.tolist()
            }

    bundle = {"model": best_model, "label_encoder": le}
    joblib.dump(bundle, MODEL_PATH)
    with open(METRICS_JSON, "w", encoding="utf-8") as f:
        json.dump(best_metrics, f, indent=2, ensure_ascii=False)

    print(f" Modelo {best_metrics['model']} guardado en {MODEL_PATH}")
    print(" Métricas registradas en MLflow (carpeta ./mlruns)")

if __name__ == "__main__":
    main()
