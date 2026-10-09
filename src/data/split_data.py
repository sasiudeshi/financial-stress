"""Add a stratified train/test split column to both feature files.

Performs ONE stratified 80/20 split (stratified by
financial_stress_level_encoded, random_state=42) and writes the resulting
'split' column ('train'/'test') into BOTH data/processed/features_unscaled.csv
and data/processed/features_scaled.csv in place, matched by user_id, so both
variants share identical row membership per split. This is required so
models trained on the scaled vs. unscaled file are still evaluated on the
exact same held-out users.
"""
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_COLUMN = "financial_stress_level_encoded"


def main():
    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    assert list(unscaled_df["user_id"]) == list(scaled_df["user_id"]), (
        "features_unscaled.csv and features_scaled.csv must have identical "
        "row order (same user_id sequence) for the split to line up."
    )

    train_ids, test_ids = train_test_split(
        unscaled_df["user_id"],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=unscaled_df[TARGET_COLUMN],
    )
    train_id_set = set(train_ids)

    split_map = unscaled_df["user_id"].apply(lambda uid: "train" if uid in train_id_set else "test")

    unscaled_df["split"] = split_map
    scaled_df["split"] = scaled_df["user_id"].apply(
        lambda uid: "train" if uid in train_id_set else "test"
    )

    unscaled_df.to_csv(UNSCALED_PATH, index=False)
    scaled_df.to_csv(SCALED_PATH, index=False)

    print(f"Split applied: train={len(train_ids)}, test={len(test_ids)}")
    print("Train class distribution:")
    print(unscaled_df.loc[unscaled_df["split"] == "train", TARGET_COLUMN].value_counts().sort_index())
    print("Test class distribution:")
    print(unscaled_df.loc[unscaled_df["split"] == "test", TARGET_COLUMN].value_counts().sort_index())
    print(f"Updated {UNSCALED_PATH}")
    print(f"Updated {SCALED_PATH}")


if __name__ == "__main__":
    main()
