"""Self-check the model training/comparison/selection/explainability stage.

Usage:
    python scripts/validate_modeling.py
"""
import json
import sys
from pathlib import Path

import joblib
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
from src.evaluation.explain import explain_prediction  # noqa: E402
from src.utils import TARGET_COLUMN, get_feature_columns  # noqa: E402

UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
MODELS_DIR = REPO_ROOT / "models"
COMPARISON_PATH = REPO_ROOT / "reports" / "results" / "model_comparison.csv"
FIGURES_DIR = REPO_ROOT / "reports" / "figures"

MODEL_NAMES = ["logreg", "svm", "decision_tree", "random_forest", "xgboost"]
EXPECTED_TRAIN = 2000
EXPECTED_TEST = 500
CLASS_TOLERANCE_PCT = 2.0


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def main():
    results = []

    # 1. split column, train/test counts ~2000/500, class proportions within 2%
    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    full_pct = unscaled_df[TARGET_COLUMN].value_counts(normalize=True).sort_index() * 100

    split_ok = True
    split_reasons = []
    for name, df in [("features_unscaled.csv", unscaled_df), ("features_scaled.csv", scaled_df)]:
        if "split" not in df.columns:
            split_ok = False
            split_reasons.append(f"{name}: no 'split' column")
            continue
        n_train = int((df["split"] == "train").sum())
        n_test = int((df["split"] == "test").sum())
        if abs(n_train - EXPECTED_TRAIN) > 5 or abs(n_test - EXPECTED_TEST) > 5:
            split_ok = False
            split_reasons.append(f"{name}: train={n_train}, test={n_test} (expected ~{EXPECTED_TRAIN}/{EXPECTED_TEST})")

        for split_name in ["train", "test"]:
            subset = df[df["split"] == split_name]
            pct = subset[TARGET_COLUMN].value_counts(normalize=True).sort_index() * 100
            for cls in full_pct.index:
                diff = abs(pct.get(cls, 0) - full_pct[cls])
                if diff > CLASS_TOLERANCE_PCT:
                    split_ok = False
                    split_reasons.append(
                        f"{name}/{split_name}: class {cls} pct={pct.get(cls, 0):.2f}% vs "
                        f"full {full_pct[cls]:.2f}% (diff {diff:.2f}% > {CLASS_TOLERANCE_PCT}%)"
                    )

    check(
        results,
        "Both feature files have 'split' column, train/test ~2000/500, class proportions within 2% of full dataset",
        split_ok,
        "; ".join(split_reasons),
    )

    # 2. All 5 model .joblib files exist
    missing_models = [f"{name}.joblib" for name in MODEL_NAMES if not (MODELS_DIR / f"{name}.joblib").exists()]
    check(results, "All 5 model .joblib files exist in models/", not missing_models,
          f"missing: {missing_models}")

    # 3. model_comparison.csv exists with exactly 5 rows and required columns
    if not COMPARISON_PATH.exists():
        check(results, "model_comparison.csv exists with 5 rows and required columns", False,
              f"{COMPARISON_PATH} not found")
    else:
        comparison_df = pd.read_csv(COMPARISON_PATH)
        required_cols = ["accuracy", "f1_macro", "recall_high_stress"]
        missing_cols = [c for c in required_cols if c not in comparison_df.columns]
        check(
            results,
            "model_comparison.csv exists with exactly 5 rows and includes accuracy/f1_macro/recall_high_stress",
            len(comparison_df) == 5 and not missing_cols,
            f"rows={len(comparison_df)}, missing columns={missing_cols}",
        )

    # 4. best_model.joblib + metadata exist, feature list matches what model was trained on
    best_model_path = MODELS_DIR / "best_model.joblib"
    metadata_path = MODELS_DIR / "best_model_metadata.json"

    if not best_model_path.exists() or not metadata_path.exists():
        check(results, "best_model.joblib and best_model_metadata.json exist with matching feature list",
              False, f"missing: {[p for p in [best_model_path, metadata_path] if not p.exists()]}")
    else:
        best_model = joblib.load(best_model_path)
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata_features = metadata["feature_columns"]

        if hasattr(best_model, "feature_names_in_"):
            trained_features = list(best_model.feature_names_in_)
        else:
            source = "scaled" if metadata["scaling_required"] else "unscaled"
            df = pd.read_csv(SCALED_PATH if source == "scaled" else UNSCALED_PATH)
            trained_features = get_feature_columns(df)

        missing_from_metadata = set(trained_features) - set(metadata_features)
        extra_in_metadata = set(metadata_features) - set(trained_features)
        order_matches = metadata_features == trained_features

        check(
            results,
            "best_model.joblib and best_model_metadata.json exist, metadata feature list matches trained model exactly",
            not missing_from_metadata and not extra_in_metadata and order_matches,
            f"missing_from_metadata={sorted(missing_from_metadata)}, "
            f"extra_in_metadata={sorted(extra_in_metadata)}, order_matches={order_matches}",
        )

    # 5. figures exist and non-empty
    fi_path = FIGURES_DIR / "feature_importance.png"
    shap_path = FIGURES_DIR / "shap_summary.png"
    fig_reasons = []
    for p in [fi_path, shap_path]:
        if not p.exists():
            fig_reasons.append(f"{p} does not exist")
        elif p.stat().st_size == 0:
            fig_reasons.append(f"{p} is empty (0 bytes)")
    check(results, "feature_importance.png and shap_summary.png both exist and are non-empty", not fig_reasons,
          "; ".join(fig_reasons))

    # 6. explain_prediction() ran on all 3 sample users without error, exactly 3 factors each
    explain_errors = []
    feature_columns = None
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        feature_columns = metadata["feature_columns"]
    except Exception as e:
        explain_errors.append(f"could not load metadata: {e}")

    if feature_columns is not None:
        test_df = unscaled_df[unscaled_df["split"] == "test"].reset_index(drop=True)
        for target_class in [0, 1, 2]:
            matches = test_df[test_df[TARGET_COLUMN] == target_class]
            if matches.empty:
                explain_errors.append(f"no test-set user found for class {target_class}")
                continue
            row = matches.iloc[0]
            user_features = {c: row[c] for c in feature_columns}
            try:
                factors = explain_prediction(user_features)
                if len(factors) != 3:
                    explain_errors.append(
                        f"class {target_class} user {row['user_id']}: expected 3 factors, got {len(factors)}"
                    )
            except Exception as e:
                explain_errors.append(f"class {target_class} user {row['user_id']}: raised {type(e).__name__}: {e}")

    check(
        results,
        "explain_prediction() ran on all 3 sample users without error, returned exactly 3 factors each",
        not explain_errors,
        "; ".join(explain_errors),
    )

    print("=== Model Training/Comparison/Selection/Explainability Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
