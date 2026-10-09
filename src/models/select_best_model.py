"""Select the best model to carry forward and persist it with metadata.

Reads reports/results/model_comparison.csv, applies the selection
reasoning (see reports/results/model_selection.md), copies the chosen
model's .joblib to models/best_model.joblib, and writes
models/best_model_metadata.json recording which feature file it needs,
the exact ordered feature column list it expects, and whether scaling is
required.
"""
import json
import shutil
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.evaluation.evaluate_models import MODEL_FEATURE_SOURCE  # noqa: E402
from src.utils import REPO_ROOT, TARGET_COLUMN, get_feature_columns  # noqa: E402

COMPARISON_PATH = REPO_ROOT / "reports" / "results" / "model_comparison.csv"
MODELS_DIR = REPO_ROOT / "models"
UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
SELECTION_MD_PATH = REPO_ROOT / "reports" / "results" / "model_selection.md"

SELECTED_MODEL_NAME = "logreg"

SELECTION_REASONING = """\
# Model Selection

**Selected model: Logistic Regression**

Across the five candidates, SVM edges out Logistic Regression on raw
F1-macro (0.776 vs 0.765) and High-stress recall (0.70 vs 0.69), but the
margins are small (roughly one percentage point), and Logistic Regression
actually has the best macro ROC-AUC of all five models (0.915), the
second-best High-stress F1 (0.746, behind only SVM's 0.753), and clearly
outperforms the tree-based models (Decision Tree, Random Forest, XGBoost)
on every headline metric. On interpretability and inference speed,
Logistic Regression is the clear winner: its coefficients are directly
readable (each standardized feature's contribution to each class is a
single number), it integrates naturally with SHAP's efficient linear
explainer, and it predicts roughly 60x faster than the RBF-kernel SVM in
a benchmark on the same 500-row test set (~1.4ms vs ~84ms) — relevant
given the proposal's own requirement for a responsive, explainable
user-facing prototype that reports "key contributing factors" per
prediction (Stage 4: Demonstration) and addresses the explainability
research gap (Gap 4). Given SVM's advantage is marginal and comes at the
cost of both interpretability and a two-order-of-magnitude slowdown at
inference, Logistic Regression is recommended as the model to carry
forward into the prototype.
"""


def main():
    comparison_df = pd.read_csv(COMPARISON_PATH)
    print("Model comparison (sorted by f1_macro):")
    print(
        comparison_df[
            ["model", "accuracy", "f1_macro", "recall_high_stress", "f1_high_stress", "roc_auc_macro_ovr"]
        ].sort_values("f1_macro", ascending=False).to_string(index=False)
    )
    print()

    source = MODEL_FEATURE_SOURCE[SELECTED_MODEL_NAME]
    feature_df = pd.read_csv(SCALED_PATH if source == "scaled" else UNSCALED_PATH)
    feature_columns = get_feature_columns(feature_df)

    src_path = MODELS_DIR / f"{SELECTED_MODEL_NAME}.joblib"
    dst_path = MODELS_DIR / "best_model.joblib"
    shutil.copyfile(src_path, dst_path)

    metadata = {
        "model_name": SELECTED_MODEL_NAME,
        "feature_file": f"data/processed/features_{source}.csv",
        "feature_columns": feature_columns,
        "scaling_required": source == "scaled",
        "scaler_path": "models/scaler.joblib" if source == "scaled" else None,
        "target_column": TARGET_COLUMN,
        "class_mapping": {"0": "Low", "1": "Moderate", "2": "High"},
    }

    metadata_path = MODELS_DIR / "best_model_metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    SELECTION_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    SELECTION_MD_PATH.write_text(SELECTION_REASONING, encoding="utf-8")

    print(f"Selected model: {SELECTED_MODEL_NAME}")
    print(f"Copied {src_path} -> {dst_path}")
    print(f"Metadata written to {metadata_path}")
    print(f"Selection reasoning written to {SELECTION_MD_PATH}")


if __name__ == "__main__":
    main()
