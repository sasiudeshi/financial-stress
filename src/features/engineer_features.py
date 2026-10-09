"""Engineer modeling features from the cleaned financial stress dataset.

Loads data/processed/cleaned_data.csv and produces two feature sets:
- data/processed/features_unscaled.csv (for tree-based models)
- data/processed/features_scaled.csv (StandardScaler applied to continuous
  numeric columns only, for Logistic Regression / SVM)

The fitted StandardScaler is saved to models/scaler.joblib so the same
transform can be re-applied to new data at inference time.

Limitation (ties to proposal Limitation #7 and #9): the proposal's Feature
Engineering section also lists "spending growth rate" (month-over-month
change) and "savings consistency" (variability of saving behavior over
time) as candidate features. Both require multi-month time series per
user. This dataset is cross-sectional (one row per user, no repeated
observations over time), so those two features cannot be constructed here
and are intentionally omitted.
"""
from pathlib import Path

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CLEANED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"
UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
SCALER_PATH = REPO_ROOT / "models" / "scaler.joblib"

OUTLIER_FLAG_COLUMNS = [
    "is_outlier_income",
    "is_outlier_expenditure",
    "is_outlier_savings",
    "is_outlier_debt_repayment",
]

STRESS_LEVEL_MAP = {"Low": 0, "Moderate": 1, "High": 2}
CAN_SAVE_MAP = {"No": 0, "Sometimes": 1, "Yes": 2}

# Columns produced by categorical encoding — excluded from StandardScaler
# because they are one-hot indicators or small ordinal/label codes, not
# continuous quantities.
NON_SCALED_ENCODED_COLUMNS = [
    "can_save_regularly_encoded",
    "financial_stress_level_encoded",
]


def engineer_ratio_features(df):
    # monthly_income and monthly_expenditure are denominators for these
    # ratios. Division by zero is mathematically undefined (0/0 -> NaN,
    # nonzero/0 -> inf in pandas -- it will NOT raise), and a NaN/inf
    # silently entering the scaler or the model would either crash later
    # with an opaque error deep in sklearn, or worse, silently produce a
    # nonsense prediction. Both are guarded against upstream (clean_data.py
    # removes monthly_income <= 0 rows; the API's Pydantic model requires
    # monthly_income > 0 and monthly_expenditure >= 0), so hitting this in
    # practice means a data integrity bug -- fail loudly here rather than
    # let it propagate as silent NaN/inf.
    if (df["monthly_income"] <= 0).any():
        raise ValueError("engineer_ratio_features: monthly_income must be > 0 for all rows")
    if (df["monthly_expenditure"] <= 0).any():
        raise ValueError("engineer_ratio_features: monthly_expenditure must be > 0 for all rows")

    df["spending_to_income_ratio"] = df["monthly_expenditure"] / df["monthly_income"]
    df["savings_ratio"] = df["savings"] / df["monthly_income"]
    df["debt_to_income_ratio"] = df["debt_repayment"] / df["monthly_income"]
    df["discretionary_ratio"] = df["non_essential_expenditure"] / df["monthly_expenditure"]
    df["essential_ratio"] = df["essential_expenditure"] / df["monthly_expenditure"]
    df["subscription_burden"] = df["subscription_expenditure"] / df["monthly_income"]
    df["spending_volatility_ratio"] = df["spending_volatility"] / df["monthly_income"]
    return df


RATIO_FEATURE_COLUMNS = [
    "spending_to_income_ratio",
    "savings_ratio",
    "debt_to_income_ratio",
    "discretionary_ratio",
    "essential_ratio",
    "subscription_burden",
    "spending_volatility_ratio",
]


def encode_categoricals(df):
    # employment_status -> one-hot
    employment_dummies = pd.get_dummies(
        df["employment_status"], prefix="employment_status"
    ).astype(int)
    df = pd.concat([df.drop(columns=["employment_status"]), employment_dummies], axis=1)

    # can_save_regularly -> ordinal
    df["can_save_regularly_encoded"] = df["can_save_regularly"].map(CAN_SAVE_MAP)
    df = df.drop(columns=["can_save_regularly"])

    # financial_stress_level -> label-encoded column, keep original string too
    df["financial_stress_level_encoded"] = df["financial_stress_level"].map(STRESS_LEVEL_MAP)

    employment_columns = list(employment_dummies.columns)
    return df, employment_columns


def main():
    df = pd.read_csv(CLEANED_PATH)

    df = engineer_ratio_features(df)
    df, employment_columns = encode_categoricals(df)

    # Modeling feature set excludes identifiers, the string target label,
    # and the outlier flag columns (kept only as reference metadata).
    non_feature_columns = ["user_id", "financial_stress_level"] + OUTLIER_FLAG_COLUMNS

    unscaled_df = df.copy()
    unscaled_df.to_csv(UNSCALED_PATH, index=False)

    # Continuous numeric columns to scale: all numeric feature columns
    # except one-hot / ordinal / label-encoded categorical columns, the
    # outlier flags, and identifiers/target.
    exclude_from_scaling = set(
        non_feature_columns + employment_columns + NON_SCALED_ENCODED_COLUMNS
    )
    numeric_columns = df.select_dtypes(include="number").columns
    scale_columns = [c for c in numeric_columns if c not in exclude_from_scaling]

    scaler = StandardScaler()
    scaled_df = df.copy()
    scaled_df[scale_columns] = scaler.fit_transform(df[scale_columns])
    scaled_df.to_csv(SCALED_PATH, index=False)

    SCALER_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, SCALER_PATH)

    print(f"Loaded {len(df)} rows from {CLEANED_PATH}")
    print(f"Engineered ratio features: {RATIO_FEATURE_COLUMNS}")
    print(f"One-hot employment columns: {employment_columns}")
    print(f"Scaled {len(scale_columns)} continuous numeric columns")
    print(f"Unscaled features written to {UNSCALED_PATH}")
    print(f"Scaled features written to {SCALED_PATH}")
    print(f"Scaler saved to {SCALER_PATH}")


if __name__ == "__main__":
    main()
