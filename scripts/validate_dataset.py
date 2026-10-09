"""Validate a financial stress dataset CSV against docs/data_dictionary.md.

Usage:
    python scripts/validate_dataset.py <path_to_csv>
"""
import argparse
import re
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DICT_PATH = REPO_ROOT / "docs" / "data_dictionary.md"

EXPECTED_ROWS = 2500
EXPECTED_COLUMNS = 35
EXPECTED_CLASS_COUNTS = {"Low": 870, "Moderate": 1132, "High": 498}

EXPECTED_BREAKDOWN = [
    "housing_expenditure", "utility_expenditure", "food_expenditure",
    "healthcare_expenditure", "education_expenditure", "transportation_expenditure",
    "shopping_expenditure", "entertainment_expenditure", "subscription_expenditure",
    "other_expenditure",
]


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def dict_columns_from(dict_text):
    table_section = dict_text.split("## Columns")[1].split("## Target Variable Creation")[0]
    table_lines = [ln for ln in table_section.splitlines() if ln.strip().startswith("|")]

    columns = []
    for line in table_lines:
        cols_in_line = re.findall(r"`([^`]+)`", line)
        if not cols_in_line:
            continue
        if ("…" in line or "..." in line) and len(cols_in_line) >= 2:
            columns.extend(EXPECTED_BREAKDOWN)
        else:
            columns.append(cols_in_line[0])
    return columns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Path to the dataset CSV to validate")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    results = []

    check(results, "Row count == %d" % EXPECTED_ROWS, len(df) == EXPECTED_ROWS,
          f"got {len(df)} rows")

    check(results, "Column count == %d" % EXPECTED_COLUMNS, len(df.columns) == EXPECTED_COLUMNS,
          f"got {len(df.columns)} columns")

    actual_counts = df["financial_stress_level"].value_counts().to_dict() \
        if "financial_stress_level" in df.columns else {}
    counts_match = all(actual_counts.get(k) == v for k, v in EXPECTED_CLASS_COUNTS.items()) \
        and len(actual_counts) == len(EXPECTED_CLASS_COUNTS)
    expected_str = ", ".join(f"{k}={v}" for k, v in EXPECTED_CLASS_COUNTS.items())
    check(results, f"financial_stress_level value counts == {expected_str}",
          counts_match, f"got {actual_counts}")

    n_missing = int(df.isnull().sum().sum())
    check(results, "No missing values (df.isnull().sum().sum() == 0)", n_missing == 0,
          f"found {n_missing} missing values")

    if DICT_PATH.exists():
        dict_text = DICT_PATH.read_text(encoding="utf-8")
        dict_columns_set = set(dict_columns_from(dict_text))
        csv_columns_set = set(df.columns)

        missing_in_csv = dict_columns_set - csv_columns_set
        extra_in_csv = csv_columns_set - dict_columns_set

        cols_match = not missing_in_csv and not extra_in_csv
        reason_parts = []
        if missing_in_csv:
            reason_parts.append(f"missing from CSV: {sorted(missing_in_csv)}")
        if extra_in_csv:
            reason_parts.append(f"unexpected extra columns in CSV: {sorted(extra_in_csv)}")
        check(results, "All data_dictionary.md columns present in CSV, no unexpected extras",
              cols_match, "; ".join(reason_parts))
    else:
        check(results, "All data_dictionary.md columns present in CSV, no unexpected extras",
              False, f"data dictionary not found at {DICT_PATH}")

    print(f"=== Dataset Self-Check: {args.csv_path} ===")
    for line in results:
        print(line)

    all_passed = all("[PASS]" in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
