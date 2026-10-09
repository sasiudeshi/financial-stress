# Data Cleaning Log

Generated: 2026-08-15T21:19:34
Source: `data\raw\synthetic_financial_data.csv`
Original row count: 2500

## 1. Duplicate Rows

0 duplicate rows found. No rows removed.

## 2. Invalid Values

- `age outside 18-100`: 0 invalid values found.
- `monthly_income <= 0`: 0 invalid values found.
- `monthly_expenditure < 0`: 0 invalid values found.
- `debt_repayment < 0`: 0 invalid values found.
- `num_financial_commitments < 0`: 0 invalid values found.
- `transaction_frequency < 0`: 0 invalid values found.
- `impulse_purchase_frequency < 0`: 0 invalid values found.
- `online_purchase_frequency < 0`: 0 invalid values found.
- `unplanned_expenditure_frequency < 0`: 0 invalid values found.
- `budget_exceed_frequency_last3mo < 0`: 0 invalid values found.
- `balance_check_frequency_per_week < 0`: 0 invalid values found.

No invalid values found overall. No rows removed for invalidity.

## 3. Outlier Detection (IQR method, flagged only — not removed)

- `is_outlier_income` (based on `monthly_income`): Q1=31800.00, Q3=83325.00, IQR=51525.00, bounds=[-45487.50, 160612.50], 61 rows flagged.
- `is_outlier_expenditure` (based on `monthly_expenditure`): Q1=22065.00, Q3=60017.50, IQR=37952.50, bounds=[-34863.75, 116946.25], 62 rows flagged.
- `is_outlier_savings` (based on `savings`): Q1=-134.86, Q3=12910.94, IQR=13045.80, bounds=[-19703.56, 32479.64], 156 rows flagged.
- `is_outlier_debt_repayment` (based on `debt_repayment`): Q1=3886.61, Q3=15153.13, IQR=11266.53, bounds=[-13013.19, 32052.93], 94 rows flagged.

## Summary

- Original row count: 2500
- Duplicate rows removed: 0
- Invalid-value rows removed: 0
- Final row count: 2500
- Output written to: `data\processed\cleaned_data.csv`
