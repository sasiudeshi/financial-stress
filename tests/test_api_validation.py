"""API input validation / robustness tests.

Covers malicious and malformed input: SQL-injection-style strings,
absurdly large numbers, invalid negatives, wrong types, an empty body, an
oversized/junk payload, and every required field missing one at a time.
Every case must be rejected with a clean 4xx and must never leak an
internal file path, stack trace, or raw exception message.
"""
import copy

import pytest

from src.utils import REPO_ROOT

SQLI_STRING = "'; DROP TABLE users; --"

# Substrings that would indicate an internal detail leaked into the
# response body -- none of these should ever appear in any error response.
LEAK_INDICATORS = [
    str(REPO_ROOT).lower(),
    "traceback",
    "site-packages",
    "line ",
    ".py\"",
    "raise ",
    "\\src\\",
    "/src/",
]


def assert_clean_4xx(response):
    assert 400 <= response.status_code < 500, (
        f"expected a 4xx response, got {response.status_code}: {response.text[:300]}"
    )
    body_lower = response.text.lower()
    for indicator in LEAK_INDICATORS:
        assert indicator not in body_lower, (
            f"response leaked internal detail ({indicator!r}): {response.text[:300]}"
        )


def assert_clean_error_response(response):
    """Weaker check for the 500/503 safety-net paths: still must not leak
    internals, whatever the status code."""
    body_lower = response.text.lower()
    for indicator in LEAK_INDICATORS:
        assert indicator not in body_lower, (
            f"response leaked internal detail ({indicator!r}): {response.text[:300]}"
        )


MALFORMED_CASES = {
    "sql_injection_in_employment_status": lambda p: {**p, "employment_status": SQLI_STRING},
    "sql_injection_in_can_save_regularly": lambda p: {**p, "can_save_regularly": SQLI_STRING},
    "sql_injection_where_int_expected": lambda p: {**p, "age": SQLI_STRING},
    "extremely_large_number": lambda p: {**p, "monthly_income": 1e20},
    "negative_where_invalid_debt": lambda p: {**p, "debt_repayment": -500.0},
    "negative_where_invalid_income": lambda p: {**p, "monthly_income": -1000.0},
    "wrong_type_string_for_float": lambda p: {**p, "monthly_income": "not_a_number"},
    "wrong_type_int_for_enum": lambda p: {**p, "can_save_regularly": 12345},
    "age_below_minimum": lambda p: {**p, "age": 15},
    "age_far_out_of_range": lambda p: {**p, "age": -5},
    "transaction_frequency_zero": lambda p: {**p, "transaction_frequency": 0},
    "budget_exceed_out_of_range": lambda p: {**p, "budget_exceed_frequency_last3mo": 4},
}


@pytest.mark.parametrize("case_name", list(MALFORMED_CASES.keys()))
def test_malformed_input_rejected_with_clean_4xx(client, valid_payload, case_name):
    mutate = MALFORMED_CASES[case_name]
    bad_payload = mutate(copy.deepcopy(valid_payload))
    response = client.post("/predict", json=bad_payload)
    assert_clean_4xx(response)


def test_empty_request_body_rejected(client):
    response = client.post("/predict", json={})
    assert_clean_4xx(response)


def test_completely_empty_body_rejected(client):
    response = client.post("/predict", content=b"", headers={"Content-Type": "application/json"})
    assert_clean_4xx(response)


def test_oversized_junk_payload_rejected(client, valid_payload):
    # A valid payload plus one huge unexpected field. extra="forbid" on the
    # Pydantic model means this is rejected outright, not silently ignored.
    bloated = copy.deepcopy(valid_payload)
    bloated["__junk__"] = "A" * (2 * 1024 * 1024)  # 2MB garbage string
    response = client.post("/predict", json=bloated)
    assert_clean_4xx(response)


@pytest.mark.parametrize("missing_field", [
    "age", "employment_status", "dependents", "monthly_income", "monthly_expenditure",
    "essential_expenditure", "non_essential_expenditure", "housing_expenditure",
    "utility_expenditure", "food_expenditure", "healthcare_expenditure", "education_expenditure",
    "transportation_expenditure", "shopping_expenditure", "entertainment_expenditure",
    "subscription_expenditure", "other_expenditure", "debt_repayment", "num_financial_commitments",
    "savings", "planned_expenditure", "transaction_frequency", "spending_volatility",
    "impulse_purchase_frequency", "online_purchase_frequency", "unplanned_expenditure_frequency",
    "budget_exceed_frequency_last3mo", "can_save_regularly", "balance_check_frequency_per_week",
    "spending_change_during_difficulty",
])
def test_each_required_field_missing_one_at_a_time(client, valid_payload, missing_field):
    incomplete = {k: v for k, v in valid_payload.items() if k != missing_field}
    response = client.post("/predict", json=incomplete)
    assert_clean_4xx(response)

    body = response.json()
    reported_fields = {err.get("loc", [None])[-1] for err in body.get("detail", [])}
    assert missing_field in reported_fields, (
        f"expected a validation error naming '{missing_field}', got: {body}"
    )


def test_service_unavailable_path_does_not_leak_internals(client, monkeypatch, valid_payload):
    """Simulate the model-loading failure path (e.g. a missing model file on
    a fresh machine) and confirm the 503 response still stays clean."""
    import src.app.api as api_module

    def boom():
        raise FileNotFoundError(str(REPO_ROOT / "models" / "best_model.joblib"))

    monkeypatch.setattr(api_module, "_get_resources", boom)
    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 503
    assert_clean_error_response(response)
