"""Train and validate a crop classifier on a REAL labelled CSV dataset.
Usage: python -m pip install -r requirements-ml.txt
       python train_model.py --csv path/to/real_crop_data.csv --target crop
Expected numeric feature columns (at least two): ph,n,p,k,moisture,temp,organic,rainfall.
Each row must be an actual labelled observation. Do not use synthetic data for validation claims.
"""
import argparse, json, pathlib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

FEATURES = ["ph", "n", "p", "k", "moisture", "temp", "organic", "rainfall"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to real, labelled crop dataset")
    parser.add_argument("--target", default="crop")
    parser.add_argument("--output", default="model_report.json")
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    cols = [c for c in FEATURES if c in df.columns]
    if len(cols) < 2:
        raise ValueError("Dataset needs at least two recognized numeric feature columns.")
    if args.target not in df:
        raise ValueError("Missing target column: " + args.target)
    df = df.dropna(subset=[args.target]).copy()
    if len(df) < 30 or df[args.target].nunique() < 2:
        raise ValueError("Need >=30 labelled observations across >=2 crop classes.")
    X = df[cols].apply(pd.to_numeric, errors="coerce")
    y = df[args.target].astype(str)
    counts = y.value_counts()
    if counts.min() < 2:
        raise ValueError("Each crop class must have >=2 observations for stratified splitting.")
    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced"))
    ])
    pipeline.fit(Xtrain, ytrain)
    pred = pipeline.predict(Xtest)
    labels = sorted(y.unique().tolist())
    report = {
        "dataset_rows": len(df), "train_rows": len(Xtrain), "test_rows": len(Xtest),
        "feature_columns": cols, "target": args.target, "class_labels": labels,
        "holdout_accuracy": round(float(accuracy_score(ytest, pred)), 6),
        "classification_report": classification_report(ytest, pred, output_dict=True, zero_division=0),
        "confusion_matrix": confusion_matrix(ytest, pred, labels=labels).tolist(),
        "limitations": "Performance applies only to this held-out dataset. No independent field or microbiome validation."
    }
    pathlib.Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Report written:", args.output)
    print("Holdout accuracy:", report["holdout_accuracy"])
    print("WARNING: No independent agricultural field validation is implied.")

if __name__ == "__main__":
    main()
