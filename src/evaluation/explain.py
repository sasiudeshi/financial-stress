"""Plain-language explanation of a single financial stress prediction.

explain_prediction(user_features_dict) is the function meant to be reused
by the prototype app: given a dict of raw (unscaled) feature values keyed
by the same 42 modeling feature names used to train the selected model
(models/best_model_metadata.json -> feature_columns), it returns the top
3 contributing factors behind that prediction, in plain language.

Internally this loads the selected model + its metadata + the fitted
StandardScaler once (module-level cache), applies the same scaling used
at training time only to the subset of features that were actually
scaled (see models/scaler.joblib's feature_names_in_ -- one-hot and
ordinal-encoded columns are deliberately left unscaled, matching
src/features/engineer_features.py), computes SHAP values for the
instance with a linear SHAP explainer, and turns the top-3 by absolute
SHAP value into readable phrases.
"""
import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import shap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.utils import CLASS_NAMES, REPO_ROOT  # noqa: E402

MODELS_DIR = REPO_ROOT / "models"
BACKGROUND_SAMPLE_SIZE = 100
RANDOM_STATE = 42
TOP_N_FACTORS = 3

# Human-readable labels for features whose snake_case name doesn't read
# naturally on its own. Anything not listed here falls back to
# humanize_feature_name()'s generic conversion.
FEATURE_LABELS = {
    "debt_to_income_ratio": "debt-to-income ratio",
    "spending_to_income_ratio": "spending-to-income ratio",
    "savings_ratio": "savings ratio",
    "discretionary_ratio": "discretionary spending ratio",
    "essential_ratio": "essential spending ratio",
    "subscription_burden": "subscription spending relative to income",
    "spending_volatility_ratio": "spending volatility relative to income",
    "spending_volatility": "month-to-month spending volatility",
    "budget_deviation": "deviation from planned budget",
    "avg_transaction_value": "average transaction value",
    "num_financial_commitments": "number of active financial commitments",
    "unplanned_expenditure_frequency": "frequency of unplanned expenses",
    "budget_exceed_frequency_last3mo": "frequency of exceeding budget (last 3 months)",
    "balance_check_frequency_per_week": "frequency of checking account balance",
    "spending_change_during_difficulty": "reported spending change during financial difficulty",
    "impulse_purchase_frequency": "impulse purchase frequency",
    "online_purchase_frequency": "online purchase frequency",
    "transaction_frequency": "transaction frequency",
    "debt_repayment": "monthly debt repayment",
    "monthly_income": "monthly income",
    "monthly_expenditure": "monthly expenditure",
    "non_essential_expenditure": "non-essential (discretionary) expenditure",
    "essential_expenditure": "essential expenditure",
    "planned_expenditure": "planned expenditure",
    "savings": "savings",
    "dependents": "number of dependents",
    "age": "age",
    "can_save_regularly_encoded": "ability to save regularly",
}

CAN_SAVE_LEVELS = {0: "No", 1: "Sometimes", 2: "Yes"}


def humanize_feature_name(col):
    if col in FEATURE_LABELS:
        return FEATURE_LABELS[col]
    if col.startswith("employment_status_"):
        return f"employment status ({col.replace('employment_status_', '')})"
    return col.replace("_", " ")


def _load_resources():
    model = joblib.load(MODELS_DIR / "best_model.joblib")
    metadata = json.loads((MODELS_DIR / "best_model_metadata.json").read_text(encoding="utf-8"))
    feature_columns = metadata["feature_columns"]

    scaler = None
    if metadata["scaling_required"]:
        scaler = joblib.load(REPO_ROOT / metadata["scaler_path"])

    feature_path = REPO_ROOT / metadata["feature_file"]
    full_df = pd.read_csv(feature_path)
    background = (
        full_df[full_df["split"] == "train"][feature_columns]
        .sample(n=BACKGROUND_SAMPLE_SIZE, random_state=RANDOM_STATE)
        .reset_index(drop=True)
    )

    explainer = shap.Explainer(model, background, feature_names=feature_columns)

    return {
        "model": model,
        "metadata": metadata,
        "feature_columns": feature_columns,
        "scaler": scaler,
        "explainer": explainer,
    }


_RESOURCES = None


def _get_resources():
    global _RESOURCES
    if _RESOURCES is None:
        _RESOURCES = _load_resources()
    return _RESOURCES


def _scale_row(raw_row, feature_columns, scaler):
    """Apply the same StandardScaler used at training time, but only to
    the subset of feature_columns the scaler was actually fit on (i.e.
    the continuous columns) -- one-hot / ordinal columns pass through
    unscaled, matching src/features/engineer_features.py."""
    scaled_row = raw_row.copy()
    if scaler is None:
        return scaled_row

    scaled_col_index = {name: i for i, name in enumerate(scaler.feature_names_in_)}
    for col in feature_columns:
        if col in scaled_col_index:
            idx = scaled_col_index[col]
            scaled_row[col] = (raw_row[col] - scaler.mean_[idx]) / scaler.scale_[idx]
    return scaled_row


def explain_prediction(user_features_dict):
    """Return the top 3 contributing factors (plain language) for a
    single user's predicted financial stress level.

    Args:
        user_features_dict: dict mapping each of models/best_model_metadata.json's
            feature_columns to a raw (unscaled) value for one user.

    Returns:
        list[str]: exactly TOP_N_FACTORS plain-language factor descriptions,
        e.g. ["High debt-to-income ratio", "Low savings ratio", ...].
    """
    resources = _get_resources()
    model = resources["model"]
    feature_columns = resources["feature_columns"]
    scaler = resources["scaler"]
    explainer = resources["explainer"]

    missing = [c for c in feature_columns if c not in user_features_dict]
    if missing:
        raise ValueError(f"user_features_dict is missing required features: {missing}")

    raw_row = pd.Series({c: user_features_dict[c] for c in feature_columns}, dtype=float)
    scaled_row = _scale_row(raw_row, feature_columns, scaler)
    X = pd.DataFrame([scaled_row], columns=feature_columns)

    predicted_class = int(model.predict(X)[0])

    shap_values = explainer(X)
    if shap_values.values.ndim == 3:
        values = shap_values.values[0, :, predicted_class]
    else:
        values = shap_values.values[0]

    order = np.argsort(np.abs(values))[::-1][:TOP_N_FACTORS]

    factors = []
    for idx in order:
        col = feature_columns[idx]
        contribution = values[idx]
        label = humanize_feature_name(col)

        if col.startswith("employment_status_"):
            state = "is" if raw_row[col] >= 0.5 else "is not"
            factors.append(f"Employment status {state} {col.replace('employment_status_', '')}")
        elif col == "can_save_regularly_encoded":
            level = CAN_SAVE_LEVELS.get(int(round(raw_row[col])), str(raw_row[col]))
            factors.append(f"Ability to save regularly: {level}")
        else:
            # Direction relative to the population: positive standardized value = High.
            direction = "High" if scaled_row[col] >= 0 else "Low"
            factors.append(f"{direction} {label}")

    return factors


def _load_sample_user(row, feature_columns):
    return {c: row[c] for c in feature_columns}


def main():
    resources = _get_resources()
    metadata = resources["metadata"]
    feature_columns = resources["feature_columns"]
    class_mapping = {int(k): v for k, v in metadata["class_mapping"].items()}

    unscaled_df = pd.read_csv(REPO_ROOT / "data" / "processed" / "features_unscaled.csv")
    test_df = unscaled_df[unscaled_df["split"] == "test"].reset_index(drop=True)

    model = resources["model"]

    for target_class in [0, 1, 2]:
        row = test_df[test_df["financial_stress_level_encoded"] == target_class].iloc[0]
        user_features = _load_sample_user(row, feature_columns)

        raw_row = pd.Series(user_features, dtype=float)
        scaled_row = _scale_row(raw_row, feature_columns, resources["scaler"])
        X = pd.DataFrame([scaled_row], columns=feature_columns)
        predicted_class = int(model.predict(X)[0])

        factors = explain_prediction(user_features)

        print(f"=== Sample user (true class = {CLASS_NAMES[target_class]}) ===")
        print(f"user_id: {row['user_id']}")
        print(f"Input features: {json.dumps(user_features, indent=2, default=str)}")
        print(f"True label: {CLASS_NAMES[target_class]}")
        print(f"Predicted label: {class_mapping[predicted_class]}")
        print(f"Top {TOP_N_FACTORS} contributing factors:")
        for i, factor in enumerate(factors, start=1):
            print(f"  {i}. {factor}")
        print()


if __name__ == "__main__":
    main()
