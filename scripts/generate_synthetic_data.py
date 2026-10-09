"""
Synthetic Financial Behavior Dataset Generator
Project: An Intelligent Financial Stress Detection System Using User Spending Behavior

METHODOLOGY NOTE (for dissertation appendix):
Since no primary questionnaire data or suitable secondary dataset was available at
project start, this script simulates a realistic questionnaire-response dataset.

Design approach: a single hidden ("latent") financial-stress factor `s` (0=no
stress, 1=severe stress) is sampled per synthetic user. Every observable variable
(income, expenditure, savings, debt, behavioral indicators, and the financial
well-being score) is then generated as a noisy function of `s`, calibrated to
match relationships reported in the literature review:
  - Impulsive/compulsive spending negatively associated with financial well-being
    (Hasin & Zainol, 2026)
  - Financial stress can exist even when expenditure < income (motivates using
    multiple features rather than a single rule-based threshold)
  - Debt-to-income ratio, savings ratio, discretionary spending, and budget
    deviation are all theorised predictors (per proposal's Research Question 1)

Because each variable has independent noise on top of the shared latent factor,
the relationship between features and the target is realistic (learnable, but not
deterministic/trivial) -- exactly like real self-reported survey data would be.

The target label itself (financial_stress_level) is NOT finalized here. This
script outputs a continuous `financial_wellbeing_score` (0-100, CFPB-scale
direction: higher = better well-being) exactly as a real questionnaire
instrument would produce. Converting that score into Low/Moderate/High stress
categories is deliberately left to the next pipeline stage (Target Variable
Creation, per proposal Section 4), so the thresholding decision is explicit,
documented, and defensible rather than baked silently into the data generator.
"""

import numpy as np
import pandas as pd

RANDOM_SEED = 42
N_USERS = 2500


def clip(arr, lo, hi):
    return np.clip(arr, lo, hi)


def generate_dataset(n=N_USERS, seed=RANDOM_SEED):
    rng = np.random.default_rng(seed)

    # ---- Hidden latent stress factor (right-skewed: most people low/moderate) ----
    s = rng.beta(2, 3, n)

    # ---- Demographics ----
    age = rng.integers(18, 66, n)
    employment_status = rng.choice(
        ["Employed", "Self-employed", "Student", "Unemployed"],
        size=n, p=[0.55, 0.15, 0.22, 0.08]
    )
    dependents = rng.integers(0, 5, n)

    # ---- Income (LKR/month; adjust currency scale as needed) ----
    # Roughly independent of stress -- deliberately, per proposal's own argument
    # that financial stress can occur even when income is technically sufficient.
    income = rng.lognormal(mean=11.15, sigma=0.45, size=n)
    income = clip(income, 18000, 400000)
    # Employment/student status adjustment
    income = np.where(employment_status == "Student", income * 0.35, income)
    income = np.where(employment_status == "Unemployed", income * 0.25, income)
    income = np.round(income, -2)

    # ---- Expenditure ----
    expenditure_ratio = clip(0.55 + 0.40 * s + rng.normal(0, 0.08, n), 0.30, 1.35)
    total_expenditure = income * expenditure_ratio

    discretionary_share = clip(0.18 + 0.45 * s + rng.normal(0, 0.07, n), 0.05, 0.85)
    non_essential_expenditure = total_expenditure * discretionary_share
    essential_expenditure = total_expenditure - non_essential_expenditure

    # ---- Debt ----
    debt_ratio = clip(0.03 + 0.35 * s + rng.normal(0, 0.06, n), 0.0, 0.65)
    debt_repayment = income * debt_ratio
    num_financial_commitments = rng.poisson(1 + 4 * debt_ratio)
    num_financial_commitments = clip(num_financial_commitments, 0, 6)

    # ---- Savings (can be negative = deficit/debt-financed spending) ----
    savings = income - total_expenditure - debt_repayment

    # ---- Budget planning behavior ----
    planned_expenditure = total_expenditure * clip(1 - 0.15 * s + rng.normal(0, 0.05, n), 0.6, 1.15)
    budget_deviation = total_expenditure - planned_expenditure

    # ---- Transaction behavior ----
    transaction_frequency = rng.poisson(18 + 28 * s) + 1
    avg_transaction_value = total_expenditure / transaction_frequency
    spending_volatility = total_expenditure * clip(0.05 + 0.28 * s + rng.normal(0, 0.05, n), 0.02, 0.55)

    # ---- Behavioral indicators ----
    impulse_purchase_frequency = rng.poisson(1 + 8 * s)
    online_purchase_frequency = rng.poisson(2 + 10 * s)
    unplanned_expenditure_frequency = rng.poisson(0.5 + 5 * s)
    budget_exceed_frequency = rng.binomial(3, clip(0.08 + 0.75 * s, 0, 1))  # out of last 3 months

    save_prob = clip(0.85 - 0.8 * s + rng.normal(0, 0.1, n), 0, 1)
    can_save_regularly = np.where(save_prob > 0.66, "Yes",
                          np.where(save_prob > 0.33, "Sometimes", "No"))

    balance_check_frequency = rng.poisson(1 + 6 * s)  # times per week
    spending_change_during_difficulty = clip(np.round(1 + 4 * s + rng.normal(0, 0.6, n)), 1, 5).astype(int)

    # ---- Spending category breakdown (sums to total_expenditure) ----
    essential_cats = rng.dirichlet([3, 2, 2.5, 1.5, 1.2, 1.5], size=n)  # housing,utility,food,healthcare,education,transport
    housing = essential_cats[:, 0] * essential_expenditure
    utility = essential_cats[:, 1] * essential_expenditure
    food = essential_cats[:, 2] * essential_expenditure
    healthcare = essential_cats[:, 3] * essential_expenditure
    education = essential_cats[:, 4] * essential_expenditure
    transportation = essential_cats[:, 5] * essential_expenditure

    discretionary_cats = rng.dirichlet([2, 2, 1.5, 1], size=n)  # shopping,entertainment,subscription,other
    shopping = discretionary_cats[:, 0] * non_essential_expenditure
    entertainment = discretionary_cats[:, 1] * non_essential_expenditure
    subscription = discretionary_cats[:, 2] * non_essential_expenditure
    other_expenditure = discretionary_cats[:, 3] * non_essential_expenditure

    # ---- Target instrument: financial well-being score (0-100, higher = better) ----
    # CFPB Financial Well-Being Scale direction: higher score = better well-being.
    financial_wellbeing_score = clip(100 * (1 - s) + rng.normal(0, 8, n), 0, 100)

    # ---- Provisional tertile-based label (for preview only -- see docstring) ----
    q1, q2 = np.quantile(financial_wellbeing_score, [1 / 3, 2 / 3])
    financial_stress_level_preview = np.where(
        financial_wellbeing_score >= q2, "Low",
        np.where(financial_wellbeing_score >= q1, "Moderate", "High")
    )

    df = pd.DataFrame({
        "user_id": [f"U{100000+i}" for i in range(n)],
        "age": age,
        "employment_status": employment_status,
        "dependents": dependents,
        "monthly_income": income.round(2),
        "monthly_expenditure": total_expenditure.round(2),
        "essential_expenditure": essential_expenditure.round(2),
        "non_essential_expenditure": non_essential_expenditure.round(2),
        "housing_expenditure": housing.round(2),
        "utility_expenditure": utility.round(2),
        "food_expenditure": food.round(2),
        "healthcare_expenditure": healthcare.round(2),
        "education_expenditure": education.round(2),
        "transportation_expenditure": transportation.round(2),
        "shopping_expenditure": shopping.round(2),
        "entertainment_expenditure": entertainment.round(2),
        "subscription_expenditure": subscription.round(2),
        "other_expenditure": other_expenditure.round(2),
        "debt_repayment": debt_repayment.round(2),
        "num_financial_commitments": num_financial_commitments,
        "savings": savings.round(2),
        "planned_expenditure": planned_expenditure.round(2),
        "budget_deviation": budget_deviation.round(2),
        "transaction_frequency": transaction_frequency,
        "avg_transaction_value": avg_transaction_value.round(2),
        "spending_volatility": spending_volatility.round(2),
        "impulse_purchase_frequency": impulse_purchase_frequency,
        "online_purchase_frequency": online_purchase_frequency,
        "unplanned_expenditure_frequency": unplanned_expenditure_frequency,
        "budget_exceed_frequency_last3mo": budget_exceed_frequency,
        "can_save_regularly": can_save_regularly,
        "balance_check_frequency_per_week": balance_check_frequency,
        "spending_change_during_difficulty": spending_change_during_difficulty,
        "financial_wellbeing_score": financial_wellbeing_score.round(1),
        "financial_stress_level_preview": financial_stress_level_preview,
    })

    return df


if __name__ == "__main__":
    df = generate_dataset()
    out_path = "/home/claude/financial_stress_project/data/synthetic_financial_data.csv"
    df.to_csv(out_path, index=False)
    print(f"Generated {len(df)} records -> {out_path}")
    print("\nClass balance (preview label):")
    print(df["financial_stress_level_preview"].value_counts())
    print("\nSummary stats:")
    print(df[["monthly_income", "monthly_expenditure", "savings", "debt_repayment",
               "financial_wellbeing_score"]].describe().round(1))
