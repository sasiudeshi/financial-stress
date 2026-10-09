# Synthetic Dataset — Data Dictionary & Generation Methodology

**File:** `synthetic_financial_data.csv`
**Records:** 2,500 synthetic users
**Generator:** `scripts/generate_synthetic_data.py` (seed=42, fully reproducible)

## Why synthetic data, and how it was built

No primary questionnaire data or suitable secondary dataset was available at
project start. Rather than fabricate values arbitrarily, this dataset was
generated using a **latent factor model**: each synthetic user is assigned a
hidden financial-stress value `s` (0 = no stress, 1 = severe stress, drawn from
a Beta(2,3) distribution so most users sit in the low/moderate range, matching
typical population distributions). Every observable column is then generated as
a function of `s` **plus independent random noise**, calibrated to match
relationships reported in the literature review (Hasin & Zainol, 2026 on
impulsive/compulsive spending; Kee et al., 2026 on e-wallet/spending behavior;
proposal's own argument that stress can exist even when expenditure < income).

This design means:
- Features correlate with the outcome the way real behavioral data would
  (learnable patterns), **not** as a deterministic formula — so models have a
  genuine classification problem to solve, not a trivial lookup.
- Monthly income is deliberately close to uncorrelated with the well-being
  score, reflecting the proposal's central argument that income alone is
  insufficient to detect stress.

**Important — this is a stated limitation, not primary data.** The dissertation
should describe this explicitly (see proposal's "Limitations of the Study",
items 1, 2, and 4) and, if time allows, validate the approach against a small
real questionnaire sample later.

## Columns

| Column | Type | Description |
|---|---|---|
| `user_id` | string | Synthetic unique identifier |
| `age` | int | 18–65 |
| `employment_status` | categorical | Employed / Self-employed / Student / Unemployed |
| `dependents` | int | Number of dependents (0–4) |
| `monthly_income` | float | Monthly income (LKR) |
| `monthly_expenditure` | float | Total monthly expenditure |
| `essential_expenditure` | float | Essential portion of expenditure |
| `non_essential_expenditure` | float | Discretionary portion of expenditure |
| `housing_expenditure` … `other_expenditure` | float | 10-category breakdown summing to `monthly_expenditure` (housing, utility, food, healthcare, education, transportation, shopping, entertainment, subscription, other) |
| `debt_repayment` | float | Monthly debt repayment obligation |
| `num_financial_commitments` | int | Number of active loans/financial commitments |
| `savings` | float | income − expenditure − debt (can be **negative** = deficit spending) |
| `planned_expenditure` | float | What the user intended to spend |
| `budget_deviation` | float | actual expenditure − planned expenditure |
| `transaction_frequency` | int | Transactions per month |
| `avg_transaction_value` | float | expenditure / transaction count |
| `spending_volatility` | float | Approximate month-to-month spending swing |
| `impulse_purchase_frequency` | int | Impulse purchases per month |
| `online_purchase_frequency` | int | Online purchases per month |
| `unplanned_expenditure_frequency` | int | Unplanned expenses per month |
| `budget_exceed_frequency_last3mo` | int (0–3) | Months out of last 3 where budget was exceeded |
| `can_save_regularly` | categorical | Yes / Sometimes / No |
| `balance_check_frequency_per_week` | int | How often the user checks their balance |
| `spending_change_during_difficulty` | int (1–5) | Self-reported spending change during financially hard periods |
| `financial_wellbeing_score` | float (0–100) | CFPB-scale-style score; **higher = better well-being** |
| `financial_stress_level` | categorical | **Final target variable.** Low / Moderate / High, assigned using fixed score bands: ≥70 = Low, 40–69 = Moderate, <40 = High. See "Target Variable Creation" below for the rationale. |

## Target Variable Creation (finalized)

The CFPB Financial Well-Being Scale does not publish an official Low/Moderate/High
cutoff — CFPB's own guidance treats the score as continuous and recommends
comparing an individual's score against national percentile benchmarks rather
than fixed categories (CFPB, "Getting started with measuring financial
well-being", 2019).

Since no official categorical cutoff exists, and a threshold derived from
tertiles of this project's own sample would be sample-dependent, this project
uses **fixed, sample-independent score bands** instead, consistent with the
"good / fair / needs attention" style bands practitioners commonly use when
reporting CFPB-scale results:

- Score ≥ 70 → **Low** financial stress
- 40 ≤ Score < 70 → **Moderate** financial stress
- Score < 40 → **High** financial stress

Resulting class distribution on this dataset: Low 34.8% (870), Moderate 45.3%
(1,132), High 19.9% (498). This is a stated, documented modelling decision —
cite it explicitly in the Methodology chapter, and re-apply the same fixed
bands consistently if real questionnaire data is collected later. Script:
`scripts/apply_target_labels.py`.

## Regenerating or adjusting

Run `python3 scripts/generate_synthetic_data.py`. To change sample size, edit
`N_USERS` at the top of the script. To change the stress distribution shape,
adjust the `Beta(2,3)` parameters — e.g. `Beta(2,2)` for a more even spread
across stress levels.
