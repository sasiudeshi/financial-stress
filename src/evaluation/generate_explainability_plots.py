"""Generate explainability artifacts for the selected best model.

Saves:
- reports/figures/feature_importance.png -- a bar chart of feature
  importance. For tree-based models this is model.feature_importances_;
  for linear models (like the selected Logistic Regression) this is the
  mean absolute standardized coefficient across the three classes, which
  is a valid importance proxy because the model is trained on scaled
  (standardized) features.
- reports/figures/shap_summary.png -- a SHAP summary (beeswarm) plot
  computed on a sample of the test set.
"""
import json
import sys
from pathlib import Path

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.utils import CLASS_NAMES, REPO_ROOT, get_feature_columns  # noqa: E402

MODELS_DIR = REPO_ROOT / "models"
FIGURES_DIR = REPO_ROOT / "reports" / "figures"
SHAP_SAMPLE_SIZE = 100
SHAP_BACKGROUND_SIZE = 100
RANDOM_STATE = 42


def plot_feature_importance(model, feature_columns):
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
    elif hasattr(model, "coef_"):
        # coef_ shape: (n_classes, n_features) for multinomial LR.
        importances = np.abs(model.coef_).mean(axis=0)
    else:
        raise ValueError(f"Model {type(model)} has neither feature_importances_ nor coef_")

    order = np.argsort(importances)[::-1]
    top_n = min(20, len(feature_columns))
    top_idx = order[:top_n]

    fig, ax = plt.subplots(figsize=(9, 8))
    ax.barh(
        [feature_columns[i] for i in top_idx][::-1],
        importances[top_idx][::-1],
        color="#3b6fa0",
    )
    ax.set_xlabel("Importance (mean |standardized coefficient| across classes)")
    ax.set_title("Feature Importance -- Logistic Regression (top 20)")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "feature_importance.png", dpi=150)
    plt.close(fig)


def plot_shap_summary(model, metadata, feature_columns):
    source = "scaled" if metadata["scaling_required"] else "unscaled"
    feature_path = REPO_ROOT / metadata["feature_file"]
    df = pd.read_csv(feature_path)

    train_df = df[df["split"] == "train"]
    test_df = df[df["split"] == "test"]

    background = train_df[feature_columns].sample(
        n=min(SHAP_BACKGROUND_SIZE, len(train_df)), random_state=RANDOM_STATE
    )
    sample = test_df[feature_columns].sample(
        n=min(SHAP_SAMPLE_SIZE, len(test_df)), random_state=RANDOM_STATE
    )

    explainer = shap.Explainer(model, background, feature_names=feature_columns)
    shap_values = explainer(sample)

    # For multiclass output, shap_values.values has shape (n_samples, n_features, n_classes).
    # Summarize with the High-stress class (index 2) since that's the class the
    # proposal cares most about detecting.
    high_class_idx = 2
    if shap_values.values.ndim == 3:
        values_for_plot = shap_values.values[:, :, high_class_idx]
        base_values = shap_values.base_values[:, high_class_idx]
    else:
        values_for_plot = shap_values.values
        base_values = shap_values.base_values

    explanation = shap.Explanation(
        values=values_for_plot,
        base_values=base_values,
        data=sample.values,
        feature_names=feature_columns,
    )

    fig = plt.figure(figsize=(9, 8))
    shap.summary_plot(explanation, sample, show=False, max_display=20)
    fig = plt.gcf()
    fig.suptitle(f"SHAP Summary -- Logistic Regression, {CLASS_NAMES[high_class_idx]}-stress class")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "shap_summary.png", dpi=150)
    plt.close(fig)


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    model = joblib.load(MODELS_DIR / "best_model.joblib")
    metadata = json.loads((MODELS_DIR / "best_model_metadata.json").read_text(encoding="utf-8"))
    feature_columns = metadata["feature_columns"]

    plot_feature_importance(model, feature_columns)
    print(f"Saved {FIGURES_DIR / 'feature_importance.png'}")

    plot_shap_summary(model, metadata, feature_columns)
    print(f"Saved {FIGURES_DIR / 'shap_summary.png'}")


if __name__ == "__main__":
    main()
