"""Self-check the FastAPI backend (src/app/api.py) using TestClient.

Usage:
    python scripts/validate_api.py
"""
import sys
from pathlib import Path

import joblib
import pandas as pd
from fastapi.testclient import TestClient

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.app.api import app  # noqa: E402
from src.evaluation.explain import _scale_row  # noqa: E402
from src.utils import CLASS_NAMES, TARGET_COLUMN  # noqa: E402

CLEANED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"
UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
MODELS_DIR = REPO_ROOT / "models"

INT_FIELDS = [
    "age", "dependents", "num_financial_commitments", "transaction_frequency",
    "impulse_purchase_frequency", "online_purchase_frequency", "unplanned_expenditure_frequency",
    "budget_exceed_frequency_last3mo", "balance_check_frequency_per_week", "spending_change_during_difficulty",
]
STR_FIELDS = ["employment_status", "can_save_regularly"]

REQUEST_FIELDS = [
    "age", "employment_status", "dependents", "monthly_income", "monthly_expenditure",
    "essential_expenditure", "non_essential_expenditure", "housing_expenditure", "utility_expenditure",
    "food_expenditure", "healthcare_expenditure", "education_expenditure", "transportation_expenditure",
    "shopping_expenditure", "entertainment_expenditure", "subscription_expenditure", "other_expenditure",
    "debt_repayment", "num_financial_commitments", "savings", "planned_expenditure", "transaction_frequency",
    "spending_volatility", "impulse_purchase_frequency", "online_purchase_frequency",
    "unplanned_expenditure_frequency", "budget_exceed_frequency_last3mo", "can_save_regularly",
    "balance_check_frequency_per_week", "spending_change_during_difficulty",
]


def row_to_payload(row):
    payload = {}
    for field in REQUEST_FIELDS:
        value = row[field]
        if field in INT_FIELDS:
            payload[field] = int(value)
        elif field in STR_FIELDS:
            payload[field] = str(value)
        else:
            payload[field] = float(value)
    return payload


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def main():
    results = []
    client = TestClient(app)

    cleaned_df = pd.read_csv(CLEANED_PATH).set_index("user_id")
    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    test_unscaled = unscaled_df[unscaled_df["split"] == "test"].reset_index(drop=True)
    scaled_by_user = scaled_df.set_index("user_id")

    model = joblib.load(MODELS_DIR / "best_model.joblib")
    from src.utils import get_feature_columns
    feature_columns = get_feature_columns(scaled_df)

    # --- 1 & 2: same 3 sample users as explain.py Step 5, compare API prediction
    # against a freshly computed reference prediction from the stored (already
    # feature-engineered) training data for that exact user.
    sample_payloads = {}
    for target_class in [0, 1, 2]:
        row = test_unscaled[test_unscaled[TARGET_COLUMN] == target_class].iloc[0]
        user_id = row["user_id"]

        cleaned_row = cleaned_df.loc[user_id]
        payload = row_to_payload(cleaned_row)
        sample_payloads[target_class] = payload

        # Reference prediction computed directly from the stored, already-scaled
        # training feature row for this user (ground truth for what the model
        # "should" say if the API engineers features identically).
        scaled_row = scaled_by_user.loc[user_id, feature_columns]
        X_ref = pd.DataFrame([scaled_row], columns=feature_columns)
        reference_class = int(model.predict(X_ref)[0])
        reference_label = CLASS_NAMES[reference_class]

        response = client.post("/predict", json=payload)
        if response.status_code != 200:
            check(
                results,
                f"Sample user {user_id} (true={CLASS_NAMES[target_class]}): API prediction matches reference",
                False,
                f"POST /predict returned {response.status_code}: {response.text}",
            )
            continue

        api_label = response.json()["financial_stress_level"]
        check(
            results,
            f"Sample user {user_id} (true={CLASS_NAMES[target_class]}): API prediction matches reference",
            api_label == reference_label,
            f"reference={reference_label}, api={api_label}",
        )

    # --- 3: 4 deliberately invalid requests -> expect 422
    baseline = sample_payloads.get(0) or next(iter(sample_payloads.values()))

    invalid_cases = {
        "negative income": {**baseline, "monthly_income": -1000.0},
        "age=15 (below minimum)": {**baseline, "age": 15},
        "invalid employment_status": {**baseline, "employment_status": "Retired"},
        "missing required field (savings)": {k: v for k, v in baseline.items() if k != "savings"},
    }

    for case_name, payload in invalid_cases.items():
        response = client.post("/predict", json=payload)
        check(
            results,
            f"Invalid request rejected with 422 ({case_name})",
            response.status_code == 422,
            f"got status {response.status_code}: {response.text}",
        )

    # --- 4: GET /health
    health_response = client.get("/health")
    health_ok = health_response.status_code == 200
    health_json = health_response.json() if health_ok else {}
    check(
        results,
        "GET /health returns 200 with model_loaded: true",
        health_ok and health_json.get("model_loaded") is True,
        f"status={health_response.status_code}, body={health_response.text}",
    )

    # --- 5: confidence scores sum to ~1.0
    response = client.post("/predict", json=baseline)
    if response.status_code == 200:
        confidence = response.json()["confidence"]
        total = sum(confidence.values())
        check(
            results,
            "Confidence scores in a successful response sum to ~1.0 (within 0.01)",
            abs(total - 1.0) <= 0.01,
            f"confidence={confidence}, sum={total}",
        )
    else:
        check(results, "Confidence scores in a successful response sum to ~1.0 (within 0.01)", False,
              f"baseline request failed with status {response.status_code}")

    print("=== API Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
