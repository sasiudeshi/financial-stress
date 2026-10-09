"""Self-check the output of src/features/engineer_features.py.

Usage:
    python scripts/validate_features.py
"""
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
CLEANED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"
UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"

RATIO_FEATURE_COLUMNS = [
    "spending_to_income_ratio",
    "savings_ratio",
    "debt_to_income_ratio",
    "discretionary_ratio",
    "essential_ratio",
    "subscription_burden",
    "spending_volatility_ratio",
]

EXPECTED_STRESS_COUNTS = {"Low": 870, "Moderate": 1132, "High": 498}
EXPECTED_STRESS_ENCODED_COUNTS = {0: 870, 1: 1132, 2: 498}

# Columns that are deliberately NOT scaled by engineer_features.py (one-hot /
# ordinal / label-encoded categoricals, identifiers, target, outlier flags) —
# excluded from the mean/std check in item 6.
NON_SCALED_COLUMNS_PREFIXES = ("employment_status_", "is_outlier_")
NON_SCALED_COLUMNS_EXACT = {
    "user_id",
    "financial_stress_level",
    "can_save_regularly_encoded",
    "financial_stress_level_encoded",
}


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def main():
    results = []

    if not CLEANED_PATH.exists():
        check(results, "cleaned_data.csv exists", False, f"{CLEANED_PATH} not found")
        print_and_exit(results)
        return

    cleaned_df = pd.read_csv(CLEANED_PATH)
    expected_rows = len(cleaned_df)

    if not UNSCALED_PATH.exists() or not SCALED_PATH.exists():
        check(
            results,
            "Both output files exist with the same row count as cleaned_data.csv",
            False,
            f"missing: {[p for p in [UNSCALED_PATH, SCALED_PATH] if not p.exists()]}",
        )
        print_and_exit(results)
        return

    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    # 1. Both output files exist with same row count as cleaned_data.csv
    rows_match = len(unscaled_df) == expected_rows and len(scaled_df) == expected_rows
    check(
        results,
        "Both output files exist with the same row count as cleaned_data.csv",
        rows_match,
        f"cleaned={expected_rows}, unscaled={len(unscaled_df)}, scaled={len(scaled_df)}",
    )

    # 2. Zero missing values in either file
    n_missing_unscaled = int(unscaled_df.isnull().sum().sum())
    n_missing_scaled = int(scaled_df.isnull().sum().sum())
    check(
        results,
        "Zero missing values in either file",
        n_missing_unscaled == 0 and n_missing_scaled == 0,
        f"unscaled missing={n_missing_unscaled}, scaled missing={n_missing_scaled}",
    )

    # 3. All 7 engineered ratio columns present in both files
    missing_unscaled = [c for c in RATIO_FEATURE_COLUMNS if c not in unscaled_df.columns]
    missing_scaled = [c for c in RATIO_FEATURE_COLUMNS if c not in scaled_df.columns]
    check(
        results,
        "All 7 engineered ratio columns are present in both files",
        not missing_unscaled and not missing_scaled,
        f"missing from unscaled={missing_unscaled}, missing from scaled={missing_scaled}",
    )

    # 4. One-hot employment columns present (print their names)
    employment_columns = [c for c in unscaled_df.columns if c.startswith("employment_status_")]
    check(
        results,
        "One-hot employment columns are present",
        len(employment_columns) > 0,
        "no employment_status_* columns found",
    )
    results.append(f"  employment columns: {employment_columns}")

    # 5. financial_stress_level_encoded only {0,1,2}, value counts match Low=870/Moderate=1132/High=498
    if "financial_stress_level_encoded" not in unscaled_df.columns:
        check(results, "financial_stress_level_encoded valid and matches expected class counts",
              False, "financial_stress_level_encoded column missing")
    else:
        encoded = unscaled_df["financial_stress_level_encoded"]
        valid_values = set(encoded.unique()) <= {0, 1, 2}
        encoded_counts = encoded.value_counts().to_dict()
        counts_match = all(
            encoded_counts.get(k) == v for k, v in EXPECTED_STRESS_ENCODED_COUNTS.items()
        ) and len(encoded_counts) == len(EXPECTED_STRESS_ENCODED_COUNTS)
        check(
            results,
            "financial_stress_level_encoded contains only {0,1,2} and counts match Low=870/Moderate=1132/High=498",
            valid_values and counts_match,
            f"unique values={sorted(encoded.unique().tolist())}, counts={encoded_counts}",
        )

    # 6. In features_scaled.csv, scaled numeric columns have mean ~0 (within 0.01), std ~1 (within 0.05)
    numeric_columns = scaled_df.select_dtypes(include="number").columns
    scale_check_columns = [
        c for c in numeric_columns
        if c not in NON_SCALED_COLUMNS_EXACT
        and not any(c.startswith(p) for p in NON_SCALED_COLUMNS_PREFIXES)
    ]

    bad_columns = []
    for col in scale_check_columns:
        mean = scaled_df[col].mean()
        std = scaled_df[col].std(ddof=0)
        if abs(mean) > 0.01 or abs(std - 1) > 0.05:
            bad_columns.append(f"{col} (mean={mean:.4f}, std={std:.4f})")

    check(
        results,
        f"Scaled numeric columns ({len(scale_check_columns)} checked) have mean ~0 (+/-0.01) and std ~1 (+/-0.05)",
        not bad_columns,
        f"out of tolerance: {bad_columns}",
    )

    print_and_exit(results)


def print_and_exit(results):
    print("=== Feature Engineering Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
