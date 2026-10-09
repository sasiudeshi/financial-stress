"""Shared constants and helpers for the modeling and evaluation scripts."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TARGET_COLUMN = "financial_stress_level_encoded"
CLASS_NAMES = {0: "Low", 1: "Moderate", 2: "High"}
CLASS_ORDER = [0, 1, 2]  # Low, Moderate, High

# Columns present in features_unscaled.csv / features_scaled.csv that are
# NOT modeling features: identifiers, the string target label, the numeric
# target itself, outlier-flag metadata, and the train/test split marker.
#
# financial_wellbeing_score is also excluded: per data_dictionary.md's
# "Target Variable Creation" section, financial_stress_level is assigned
# from financial_wellbeing_score via fixed bands (>=70 Low, 40-69 Moderate,
# <40 High) with a 1:1, zero-noise mapping. Keeping it as a feature is
# target leakage -- a model (especially a tree) just relearns the
# threshold rule instead of solving the actual spending-behavior
# classification problem the dissertation is about.
NON_FEATURE_COLUMNS = [
    "user_id",
    "financial_stress_level",
    TARGET_COLUMN,
    "financial_wellbeing_score",
    "is_outlier_income",
    "is_outlier_expenditure",
    "is_outlier_savings",
    "is_outlier_debt_repayment",
    "split",
]


def get_feature_columns(df):
    """Return the ordered list of modeling feature columns present in df."""
    return [c for c in df.columns if c not in NON_FEATURE_COLUMNS]
