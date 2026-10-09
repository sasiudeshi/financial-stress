"""Clean the raw synthetic financial dataset.

Loads data/raw/synthetic_financial_data.csv, removes exact duplicates,
checks for invalid values, flags outliers (without deleting them), and
writes the result to data/processed/cleaned_data.csv. A log of everything
found and done is written to reports/results/data_cleaning_log.md.
"""
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_PATH = REPO_ROOT / "data" / "raw" / "synthetic_financial_data.csv"
PROCESSED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"
LOG_PATH = REPO_ROOT / "reports" / "results" / "data_cleaning_log.md"

# Columns that should never be negative
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

# Columns to flag (not remove) outliers on, via IQR method
OUTLIER_COLUMNS = ["monthly_income", "monthly_expenditure", "savings", "debt_repayment"]


def find_duplicates(df):
    return df[df.duplicated(keep="first")]


def find_invalid_rows(df):
    """Return a dict of {rule_description: boolean_mask} for each invalid-value rule."""
    invalid = {}

    invalid["age outside 18-100"] = ~df["age"].between(18, 100)
    invalid["monthly_income <= 0"] = df["monthly_income"] <= 0
    invalid["monthly_expenditure < 0"] = df["monthly_expenditure"] < 0

    for col in NON_NEGATIVE_COLUMNS:
        invalid[f"{col} < 0"] = df[col] < 0

    return invalid


def flag_outliers_iqr(df, columns):
    """Add a boolean is_outlier_<feature> column per feature using the IQR method."""
    flag_columns = {}
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        flag_col = f"is_outlier_{col.replace('monthly_', '')}"
        df[flag_col] = (df[col] < lower_bound) | (df[col] > upper_bound)
        flag_columns[flag_col] = {
            "column": col,
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "count": int(df[flag_col].sum()),
        }
    return df, flag_columns


def main():
    df = pd.read_csv(RAW_PATH)
    original_row_count = len(df)

    log_lines = []
    log_lines.append("# Data Cleaning Log")
    log_lines.append("")
    log_lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}")
    log_lines.append(f"Source: `{RAW_PATH.relative_to(REPO_ROOT)}`")
    log_lines.append(f"Original row count: {original_row_count}")
    log_lines.append("")

    # 1. Duplicates
    duplicates = find_duplicates(df)
    n_duplicates = len(duplicates)
    df = df.drop_duplicates(keep="first").reset_index(drop=True)

    log_lines.append("## 1. Duplicate Rows")
    log_lines.append("")
    if n_duplicates == 0:
        log_lines.append("0 duplicate rows found. No rows removed.")
    else:
        log_lines.append(f"{n_duplicates} exact duplicate rows found and removed (kept first occurrence).")
        log_lines.append(f"Duplicate `user_id` values removed: {duplicates['user_id'].tolist()}")
    log_lines.append("")

    # 2. Invalid values
    invalid_masks = find_invalid_rows(df)
    log_lines.append("## 2. Invalid Values")
    log_lines.append("")
    total_invalid_rows = set()
    any_invalid = False
    for rule, mask in invalid_masks.items():
        n_invalid = int(mask.sum())
        if n_invalid == 0:
            log_lines.append(f"- `{rule}`: 0 invalid values found.")
        else:
            any_invalid = True
            bad_ids = df.loc[mask, "user_id"].tolist()
            log_lines.append(
                f"- `{rule}`: {n_invalid} invalid value(s) found and removed "
                f"(user_id: {bad_ids})."
            )
            total_invalid_rows.update(df.index[mask].tolist())

    if not any_invalid:
        log_lines.append("")
        log_lines.append("No invalid values found overall. No rows removed for invalidity.")
    else:
        n_removed_invalid = len(total_invalid_rows)
        df = df.drop(index=list(total_invalid_rows)).reset_index(drop=True)
        log_lines.append("")
        log_lines.append(f"Total rows removed for invalid values (union across rules): {n_removed_invalid}")
    log_lines.append("")

    # 3. Outlier flagging (IQR method) — flag only, do not delete
    df, flag_info = flag_outliers_iqr(df, OUTLIER_COLUMNS)

    log_lines.append("## 3. Outlier Detection (IQR method, flagged only — not removed)")
    log_lines.append("")
    for flag_col, info in flag_info.items():
        log_lines.append(
            f"- `{flag_col}` (based on `{info['column']}`): Q1={info['q1']:.2f}, Q3={info['q3']:.2f}, "
            f"IQR={info['iqr']:.2f}, bounds=[{info['lower_bound']:.2f}, {info['upper_bound']:.2f}], "
            f"{info['count']} rows flagged."
        )
    log_lines.append("")

    # 4. Save cleaned data
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    final_row_count = len(df)
    log_lines.append("## Summary")
    log_lines.append("")
    log_lines.append(f"- Original row count: {original_row_count}")
    log_lines.append(f"- Duplicate rows removed: {n_duplicates}")
    log_lines.append(f"- Invalid-value rows removed: {len(total_invalid_rows)}")
    log_lines.append(f"- Final row count: {final_row_count}")
    log_lines.append(f"- Output written to: `{PROCESSED_PATH.relative_to(REPO_ROOT)}`")
    log_lines.append("")

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("\n".join(log_lines), encoding="utf-8")

    print(f"Cleaned data written to {PROCESSED_PATH}")
    print(f"Log written to {LOG_PATH}")
    print(f"Rows: {original_row_count} -> {final_row_count}")


if __name__ == "__main__":
    main()
