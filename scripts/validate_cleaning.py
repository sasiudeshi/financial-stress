"""Self-check the output of src/data/clean_data.py.

Usage:
    python scripts/validate_cleaning.py
"""
import re
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = REPO_ROOT / "data" / "raw" / "synthetic_financial_data.csv"
PROCESSED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"
LOG_PATH = REPO_ROOT / "reports" / "results" / "data_cleaning_log.md"

NON_NEGATIVE_COLUMNS = [
    "debt_repayment",
    "num_financial_commitments",
    "transaction_frequency",
    "impulse_purchase_frequency",
    "online_purchase_frequency",
    "unplanned_expenditure_frequency",
    "budget_exceed_frequency_last3mo",
    "balance_check_frequency_per_week",
]

OUTLIER_FLAG_COLUMNS = [
    "is_outlier_income",
    "is_outlier_expenditure",
    "is_outlier_savings",
    "is_outlier_debt_repayment",
]


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def parse_cleaning_log(log_path):
    """Extract 'Duplicate rows removed' and 'Invalid-value rows removed' counts
    from the Summary section of data_cleaning_log.md."""
    text = log_path.read_text(encoding="utf-8")

    dupes_match = re.search(r"Duplicate rows removed:\s*(\d+)", text)
    invalid_match = re.search(r"Invalid-value rows removed:\s*(\d+)", text)

    if not dupes_match or not invalid_match:
        raise ValueError(
            f"Could not find both 'Duplicate rows removed' and 'Invalid-value rows removed' "
            f"lines in {log_path}"
        )

    return int(dupes_match.group(1)), int(invalid_match.group(1))


def main():
    results = []

    # 1. cleaned_data.csv exists and has <= rows than raw
    if not PROCESSED_PATH.exists():
        check(results, "cleaned_data.csv exists with <= rows than raw", False,
              f"{PROCESSED_PATH} does not exist")
        print_and_exit(results)
        return

    raw_df = pd.read_csv(RAW_PATH)
    df = pd.read_csv(PROCESSED_PATH)

    check(results, "cleaned_data.csv exists and has same or fewer rows than raw",
          len(df) <= len(raw_df),
          f"raw has {len(raw_df)} rows, cleaned has {len(df)} rows")

    # 2. Zero duplicate rows remain
    n_dupes = int(df.duplicated(keep="first").sum())
    check(results, "Zero duplicate rows remain", n_dupes == 0,
          f"found {n_dupes} duplicate rows")

    # 3. Zero invalid values remain
    invalid_reasons = []
    n_invalid_total = 0

    n = int((~df["age"].between(18, 100)).sum())
    n_invalid_total += n
    if n:
        invalid_reasons.append(f"age outside 18-100: {n}")

    n = int((df["monthly_income"] <= 0).sum())
    n_invalid_total += n
    if n:
        invalid_reasons.append(f"monthly_income <= 0: {n}")

    n = int((df["monthly_expenditure"] < 0).sum())
    n_invalid_total += n
    if n:
        invalid_reasons.append(f"monthly_expenditure < 0: {n}")

    for col in NON_NEGATIVE_COLUMNS:
        n = int((df[col] < 0).sum())
        n_invalid_total += n
        if n:
            invalid_reasons.append(f"{col} < 0: {n}")

    check(results, "Zero invalid values remain per the rules above", n_invalid_total == 0,
          "; ".join(invalid_reasons))

    # 4. Outlier flag columns exist, print counts
    missing_flags = [c for c in OUTLIER_FLAG_COLUMNS if c not in df.columns]
    check(results, "All four outlier flag columns exist", not missing_flags,
          f"missing: {missing_flags}")

    for flag_col in OUTLIER_FLAG_COLUMNS:
        if flag_col in df.columns:
            count = int(df[flag_col].sum())
            results.append(f"  {flag_col}: {count} flagged")

    # 5. original row count minus duplicates removed minus invalid rows removed == cleaned row count
    if not LOG_PATH.exists():
        check(
            results,
            "Original row count minus duplicates removed minus invalid rows removed equals cleaned row count",
            False,
            f"cleaning log not found at {LOG_PATH}",
        )
    else:
        n_dupes_removed, n_invalid_removed = parse_cleaning_log(LOG_PATH)
        expected_after_cleaning = len(raw_df) - n_dupes_removed - n_invalid_removed
        check(
            results,
            "Original row count minus duplicates removed minus invalid rows removed equals cleaned row count",
            expected_after_cleaning == len(df),
            f"raw={len(raw_df)}, duplicates_removed={n_dupes_removed}, "
            f"invalid_removed={n_invalid_removed}, expected={expected_after_cleaning}, "
            f"got cleaned={len(df)}",
        )

    print_and_exit(results)


def print_and_exit(results):
    print("=== Data Cleaning Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
