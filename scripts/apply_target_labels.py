"""
Target Variable Creation
Project: An Intelligent Financial Stress Detection System Using User Spending Behavior

METHODOLOGY NOTE (for dissertation Methodology / Data Preprocessing chapter):

The CFPB Financial Well-Being Scale does not publish an official Low/Moderate/High
cutoff -- CFPB's own guidance treats the score as continuous and recommends
comparing an individual's score against national percentile benchmarks (10th,
25th, 50th, 75th, 90th) rather than bucketing it into fixed categories
(CFPB, "Getting started with measuring financial well-being", 2019).

Since no official categorical cutoff exists, and since a threshold derived from
tertiles of this project's own sample would be sample-dependent (i.e. it would
shift if the sample's composition changed, which is undesirable for a label
definition), this project instead uses FIXED, sample-independent score bands,
consistent with the "good / fair / needs attention" style bands practitioners
commonly use when reporting CFPB-scale results:

    Score >= 70            -> Low financial stress
    40 <= Score < 70        -> Moderate financial stress
    Score < 40             -> High financial stress

This is a documented modelling decision, not an assumption -- it should be
stated explicitly in the dissertation, and revisited if real questionnaire
data is later collected (the same bands should be reapplied consistently).
"""

import pandas as pd

LOW_THRESHOLD = 70   # score >= this -> Low stress
HIGH_THRESHOLD = 40  # score < this -> High stress


def apply_target_label(df, score_col="financial_wellbeing_score"):
    def label(score):
        if score >= LOW_THRESHOLD:
            return "Low"
        elif score >= HIGH_THRESHOLD:
            return "Moderate"
        else:
            return "High"

    df = df.copy()
    df["financial_stress_level"] = df[score_col].apply(label)
    if "financial_stress_level_preview" in df.columns:
        df = df.drop(columns=["financial_stress_level_preview"])
    return df


if __name__ == "__main__":
    in_path = "/home/claude/financial_stress_project/data/synthetic_financial_data.csv"
    out_path = "/home/claude/financial_stress_project/data/synthetic_financial_data.csv"

    df = pd.read_csv(in_path)
    df = apply_target_label(df)
    df.to_csv(out_path, index=False)

    print(f"Applied final target label -> {out_path}")
    print("\nClass distribution:")
    counts = df["financial_stress_level"].value_counts()
    pcts = (counts / len(df) * 100).round(1)
    for cls in ["Low", "Moderate", "High"]:
        print(f"  {cls:10s}: {counts[cls]:5d}  ({pcts[cls]}%)")

    print("\nScore range check (min/max per class):")
    print(df.groupby("financial_stress_level")["financial_wellbeing_score"].agg(["min", "max", "count"]))
