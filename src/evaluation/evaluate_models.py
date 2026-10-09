"""Evaluate the 5 trained models on the held-out test split.

For each model in models/*.joblib, computes accuracy, macro precision/
recall/F1, per-class precision/recall/F1 for Low/Moderate/High, the
confusion matrix, and macro one-vs-rest ROC-AUC on the test split.
High-stress recall/F1 are reported under explicit recall_high_stress /
f1_high_stress columns since a missed high-stress user matters more than
a false alarm (per the proposal). Writes the full comparison table to
reports/results/model_comparison.csv.
"""
import json
import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.utils import CLASS_NAMES, CLASS_ORDER, REPO_ROOT, TARGET_COLUMN, get_feature_columns  # noqa: E402

UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
MODELS_DIR = REPO_ROOT / "models"
COMPARISON_PATH = REPO_ROOT / "reports" / "results" / "model_comparison.csv"

# Which feature file each model needs at inference time.
MODEL_FEATURE_SOURCE = {
    "logreg": "scaled",
    "svm": "scaled",
    "decision_tree": "unscaled",
    "random_forest": "unscaled",
    "xgboost": "unscaled",
}


def evaluate_one(name, model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)

    row = {"model": name}
    row["accuracy"] = accuracy_score(y_test, y_pred)
    row["precision_macro"] = precision_score(y_test, y_pred, average="macro", zero_division=0)
    row["recall_macro"] = recall_score(y_test, y_pred, average="macro", zero_division=0)
    row["f1_macro"] = f1_score(y_test, y_pred, average="macro", zero_division=0)

    precision_per_class = precision_score(y_test, y_pred, average=None, labels=CLASS_ORDER, zero_division=0)
    recall_per_class = recall_score(y_test, y_pred, average=None, labels=CLASS_ORDER, zero_division=0)
    f1_per_class = f1_score(y_test, y_pred, average=None, labels=CLASS_ORDER, zero_division=0)

    for i, cls in enumerate(CLASS_ORDER):
        cls_name = CLASS_NAMES[cls].lower()
        row[f"precision_{cls_name}"] = precision_per_class[i]
        row[f"recall_{cls_name}"] = recall_per_class[i]
        row[f"f1_{cls_name}"] = f1_per_class[i]

    # Explicit, clearly-labeled High-stress metrics (High = class 2).
    row["recall_high_stress"] = row["recall_high"]
    row["f1_high_stress"] = row["f1_high"]

    row["roc_auc_macro_ovr"] = roc_auc_score(
        y_test, y_proba, multi_class="ovr", average="macro", labels=CLASS_ORDER
    )

    cm = confusion_matrix(y_test, y_pred, labels=CLASS_ORDER)
    row["confusion_matrix"] = json.dumps(cm.tolist())

    return row, cm


def main():
    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    unscaled_test = unscaled_df[unscaled_df["split"] == "test"].reset_index(drop=True)
    scaled_test = scaled_df[scaled_df["split"] == "test"].reset_index(drop=True)

    assert list(unscaled_test["user_id"]) == list(scaled_test["user_id"]), (
        "Test rows must be identical (same order) across both feature files"
    )

    unscaled_features = get_feature_columns(unscaled_df)
    scaled_features = get_feature_columns(scaled_df)

    X_test_unscaled = unscaled_test[unscaled_features]
    X_test_scaled = scaled_test[scaled_features]
    y_test = unscaled_test[TARGET_COLUMN]

    rows = []
    for name, source in MODEL_FEATURE_SOURCE.items():
        model_path = MODELS_DIR / f"{name}.joblib"
        model = joblib.load(model_path)
        X_test = X_test_scaled if source == "scaled" else X_test_unscaled

        row, cm = evaluate_one(name, model, X_test, y_test)
        rows.append(row)

        print(f"=== {name} (features: {source}) ===")
        print(f"  accuracy={row['accuracy']:.4f}  f1_macro={row['f1_macro']:.4f}  "
              f"roc_auc_macro_ovr={row['roc_auc_macro_ovr']:.4f}")
        print(f"  High-stress: recall={row['recall_high_stress']:.4f}  f1={row['f1_high_stress']:.4f}")
        print(f"  Confusion matrix (rows=true, cols=pred, order=Low/Moderate/High):")
        print(f"  {cm.tolist()}")
        print()

    comparison_df = pd.DataFrame(rows)
    COMPARISON_PATH.parent.mkdir(parents=True, exist_ok=True)
    comparison_df.to_csv(COMPARISON_PATH, index=False)
    print(f"Comparison table written to {COMPARISON_PATH}")


if __name__ == "__main__":
    main()
