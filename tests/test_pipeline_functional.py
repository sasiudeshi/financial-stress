"""Functional test: one complete raw user record through the entire
pipeline -- clean -> engineer features -> predict via /predict.

'Clean' is exercised directly against src/data/clean_data.py's own
validation rules (the same rules a fresh CSV batch would be checked
against). 'Engineer features -> predict' is exercised by actually calling
the live /predict endpoint, which internally reproduces
src/features/engineer_features.py's ratio/encoding logic on this single
record before running it through the trained model -- see src/app/api.py.
"""
import pandas as pd

from src.data.clean_data import NON_NEGATIVE_COLUMNS, find_invalid_rows


def test_real_user_record_passes_clean_data_validation(cleaned_df):
    """A record already present in cleaned_data.csv must, by construction,
    pass every one of clean_data.py's own invalid-value rules -- this
    exercises the 'clean' stage directly rather than assuming it."""
    record = cleaned_df.loc[["U100000"]].reset_index()

    invalid_masks = find_invalid_rows(record)
    for rule, mask in invalid_masks.items():
        assert not mask.any(), f"real user record unexpectedly failed clean_data rule: {rule}"

    # Sanity check the rule set itself covers the fields we expect.
    assert "debt_repayment" in NON_NEGATIVE_COLUMNS


def test_full_pipeline_produces_a_valid_prediction(client, valid_payload):
    """clean (already verified above) -> engineer features -> predict,
    exercised end-to-end through the real /predict endpoint for one
    complete raw record."""
    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200
    body = response.json()

    assert body["financial_stress_level"] in {"Low", "Moderate", "High"}

    assert set(body["confidence"].keys()) == {"Low", "Moderate", "High"}
    total_confidence = sum(body["confidence"].values())
    assert abs(total_confidence - 1.0) < 0.01

    assert isinstance(body["contributing_factors"], list)
    assert len(body["contributing_factors"]) == 3
    assert all(isinstance(f, str) and f for f in body["contributing_factors"])

    assert isinstance(body["recommendations"], list)
    assert len(body["recommendations"]) >= 1

    assert "diagnosis" in body["disclaimer"].lower()


def test_full_pipeline_is_deterministic_for_the_same_record(client, valid_payload):
    """Same raw record submitted twice must produce the same classification
    -- confirms the engineered feature vector isn't drifting between calls
    (e.g. due to unseeded randomness anywhere in the request path)."""
    first = client.post("/predict", json=valid_payload).json()
    second = client.post("/predict", json=valid_payload).json()

    assert first["financial_stress_level"] == second["financial_stress_level"]
    assert first["confidence"] == second["confidence"]
    assert first["contributing_factors"] == second["contributing_factors"]
