"""FastAPI backend for the financial stress detection prototype.

POST /predict accepts raw questionnaire-style input (not pre-engineered
features) and reproduces the exact training-time feature engineering
pipeline before calling the selected model:

1. Validate input (Pydantic).
2. Engineer features exactly as src/features/engineer_features.py does:
   - the 7 ratio features, via that module's own engineer_ratio_features()
     (imported directly, not reimplemented, so the formulas can't drift)
   - one-hot encode employment_status using the same 4 category columns
     the model was trained on
   - ordinal-encode can_save_regularly with the same CAN_SAVE_MAP
   Two more model features -- budget_deviation and avg_transaction_value
   -- are raw columns from the original dataset (data_dictionary.md),
   not part of engineer_features.py's ratio step, but are derivable from
   fields in this endpoint's raw input (monthly_expenditure,
   planned_expenditure, transaction_frequency) using the exact formulas
   documented there. They are computed here for the same reason: without
   them the feature vector would not match what the model was trained on.
3. Scale the subset of columns models/scaler.joblib was actually fit on
   (src.evaluation.explain._scale_row -- the same helper explain_prediction
   itself uses, so there is exactly one implementation of this logic).
4. Reindex to models/best_model_metadata.json's exact ordered feature
   list, failing loudly (500, not a silent NaN-fill) if the engineered
   feature set doesn't match it exactly.
5. Predict class + probabilities with models/best_model.joblib.
6. Call explain_prediction() for the top-3 contributing factors.
7. Map those factors to general financial-awareness suggestions.

GET /health reports whether the model/scaler/explainer actually loaded.
"""
import logging
import sys
from pathlib import Path
from typing import Literal

from contextlib import asynccontextmanager

import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field

logger = logging.getLogger("financial_stress_api")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.evaluation.explain import _get_resources, _scale_row, explain_prediction  # noqa: E402
from src.features.engineer_features import CAN_SAVE_MAP, RATIO_FEATURE_COLUMNS, engineer_ratio_features  # noqa: E402

EMPLOYMENT_CATEGORIES = ["Employed", "Self-employed", "Student", "Unemployed"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Reuses src.evaluation.explain's module-level cache so the model,
    # scaler, and SHAP explainer are loaded exactly once and shared
    # between /predict's own model.predict() call and explain_prediction().
    try:
        _get_resources()
    except Exception:
        # Leave the cache empty; /health and /predict will report the failure.
        pass
    yield


app = FastAPI(title="Financial Stress Detection API", lifespan=lifespan)


# Upper bounds are generous relative to the training data (max monthly_income
# observed was ~293,600; see docs/data_dictionary.md) but exist specifically
# to reject absurd/adversarial values (e.g. 1e20) with a clean 422 instead of
# letting them reach the scaler/model, where a huge value could produce a
# nonsense prediction or a numerically-odd error deep inside sklearn/SHAP.
MONEY_MAX = 10_000_000.0
COUNT_MAX = 100_000


class FinancialProfileRequest(BaseModel):
    # Reject unexpected/extra fields outright (422) rather than silently
    # ignoring them -- also doubles as an oversized/junk-payload guard.
    model_config = ConfigDict(extra="forbid")

    age: int = Field(..., ge=18, le=100)
    employment_status: Literal["Employed", "Self-employed", "Student", "Unemployed"]
    dependents: int = Field(..., ge=0, le=20)
    monthly_income: float = Field(..., gt=0, le=MONEY_MAX)
    # gt=0, not ge=0: discretionary_ratio/essential_ratio divide by this
    # (see src/features/engineer_features.py's engineer_ratio_features guard).
    monthly_expenditure: float = Field(..., gt=0, le=MONEY_MAX)
    essential_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    non_essential_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    housing_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    utility_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    food_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    healthcare_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    education_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    transportation_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    shopping_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    entertainment_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    subscription_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    other_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    debt_repayment: float = Field(..., ge=0, le=MONEY_MAX)
    num_financial_commitments: int = Field(..., ge=0, le=COUNT_MAX)
    savings: float = Field(..., ge=-MONEY_MAX, le=MONEY_MAX)  # deficit spending is valid, so this may be negative
    planned_expenditure: float = Field(..., ge=0, le=MONEY_MAX)
    transaction_frequency: int = Field(..., ge=1, le=COUNT_MAX)  # >=1 avoids divide-by-zero for avg_transaction_value
    spending_volatility: float = Field(..., ge=0, le=MONEY_MAX)
    impulse_purchase_frequency: int = Field(..., ge=0, le=COUNT_MAX)
    online_purchase_frequency: int = Field(..., ge=0, le=COUNT_MAX)
    unplanned_expenditure_frequency: int = Field(..., ge=0, le=COUNT_MAX)
    budget_exceed_frequency_last3mo: int = Field(..., ge=0, le=3)
    can_save_regularly: Literal["Yes", "Sometimes", "No"]
    balance_check_frequency_per_week: int = Field(..., ge=0, le=COUNT_MAX)
    spending_change_during_difficulty: int = Field(..., ge=1, le=5)


PASSTHROUGH_FIELDS = [
    "age", "dependents", "monthly_income", "monthly_expenditure", "essential_expenditure",
    "non_essential_expenditure", "housing_expenditure", "utility_expenditure", "food_expenditure",
    "healthcare_expenditure", "education_expenditure", "transportation_expenditure", "shopping_expenditure",
    "entertainment_expenditure", "subscription_expenditure", "other_expenditure", "debt_repayment",
    "num_financial_commitments", "savings", "planned_expenditure", "transaction_frequency",
    "spending_volatility", "impulse_purchase_frequency", "online_purchase_frequency",
    "unplanned_expenditure_frequency", "budget_exceed_frequency_last3mo",
    "balance_check_frequency_per_week", "spending_change_during_difficulty",
]

# (keyword to match against a contributing-factor phrase) -> general,
# non-prescriptive financial-awareness suggestions (never professional
# advice / directives like "refinance" or "you should").
SUGGESTION_RULES = [
    ("debt-to-income", ["Consider reviewing recurring debt obligations relative to income."]),
    ("monthly debt repayment", ["Consider reviewing recurring debt obligations relative to income."]),
    ("ability to save regularly", [
        "Consider setting aside a small, consistent amount in savings each month.",
        "Consider reviewing upcoming expenses for opportunities to save regularly.",
    ]),
    ("savings", ["Consider reviewing how much of each month's income is set aside as savings."]),
    ("discretionary", ["Consider tracking discretionary purchases to see where flexibility exists."]),
    ("essential spending", ["Consider reviewing essential expenses for possible adjustments."]),
    ("subscription", ["Consider reviewing active subscriptions for ones that are no longer used."]),
    ("volatility", ["Consider tracking month-to-month spending to understand what drives fluctuations."]),
    ("deviation from planned budget", ["Consider comparing planned versus actual spending to spot patterns."]),
    ("exceeding budget", ["Consider comparing planned versus actual spending to spot patterns."]),
    ("impulse purchase", ["Consider adding a brief pause before non-essential purchases."]),
    ("online purchase", ["Consider reviewing recurring online purchase habits."]),
    ("unplanned expense", ["Consider setting aside a small buffer for unexpected expenses."]),
    ("transaction", ["Consider reviewing spending frequency and typical purchase size for patterns."]),
    ("checking account balance", ["Consider setting a regular routine for reviewing account activity."]),
    ("employment status", ["Consider exploring financial planning resources relevant to your employment situation."]),
    ("spending change during financial difficulty", [
        "Consider planning ahead for how spending might change during difficult periods."
    ]),
    ("income", ["Consider reviewing how spending aligns with overall income."]),
    ("expenditure", ["Consider reviewing this area of spending for patterns worth noting."]),
]
DEFAULT_SUGGESTION = "Consider reviewing this aspect of your spending patterns for potential adjustments."


def build_recommendations(factors):
    recommendations = []
    for factor in factors:
        factor_lower = factor.lower()
        matched = None
        for keyword, suggestions in SUGGESTION_RULES:
            if keyword in factor_lower:
                matched = suggestions
                break
        for suggestion in matched or [DEFAULT_SUGGESTION]:
            if suggestion not in recommendations:
                recommendations.append(suggestion)
    return recommendations


def engineer_request_features(request: FinancialProfileRequest, feature_columns):
    raw_input = request.model_dump()

    engineered = {field: raw_input[field] for field in PASSTHROUGH_FIELDS}

    # Raw dataset columns per data_dictionary.md, not part of
    # engineer_features.py's ratio step, but required by the trained model.
    engineered["budget_deviation"] = raw_input["monthly_expenditure"] - raw_input["planned_expenditure"]
    engineered["avg_transaction_value"] = raw_input["monthly_expenditure"] / raw_input["transaction_frequency"]

    ratio_input_df = pd.DataFrame([engineered])
    ratio_input_df = engineer_ratio_features(ratio_input_df)
    for col in RATIO_FEATURE_COLUMNS:
        engineered[col] = float(ratio_input_df.iloc[0][col])

    for category in EMPLOYMENT_CATEGORIES:
        engineered[f"employment_status_{category}"] = 1 if raw_input["employment_status"] == category else 0

    engineered["can_save_regularly_encoded"] = CAN_SAVE_MAP[raw_input["can_save_regularly"]]

    engineered_keys = set(engineered.keys())
    expected_keys = set(feature_columns)
    if engineered_keys != expected_keys:
        missing = expected_keys - engineered_keys
        extra = engineered_keys - expected_keys
        raise HTTPException(
            status_code=500,
            detail=(
                "Internal feature engineering mismatch: engineered features do not match "
                f"models/best_model_metadata.json's feature_columns. missing={sorted(missing)}, "
                f"extra={sorted(extra)}"
            ),
        )

    return engineered


@app.get("/health")
def health():
    try:
        resources = _get_resources()
        model_loaded = resources.get("model") is not None
    except Exception:
        model_loaded = False
    return {"status": "ok", "model_loaded": model_loaded}


@app.post("/predict")
def predict(request: FinancialProfileRequest):
    try:
        resources = _get_resources()
    except Exception:
        logger.exception("Failed to load model resources")
        raise HTTPException(status_code=503, detail="Model is not currently available. Please try again shortly.")

    model = resources["model"]
    metadata = resources["metadata"]
    feature_columns = resources["feature_columns"]
    scaler = resources["scaler"]
    class_mapping = {int(k): v for k, v in metadata["class_mapping"].items()}

    engineered = engineer_request_features(request, feature_columns)

    raw_row = pd.Series({c: engineered[c] for c in feature_columns}, dtype=float)
    scaled_row = _scale_row(raw_row, feature_columns, scaler)
    X = pd.DataFrame([scaled_row], columns=feature_columns)

    predicted_class = int(model.predict(X)[0])
    proba = model.predict_proba(X)[0]

    confidence = {
        class_mapping[cls]: round(float(p), 6)
        for cls, p in zip(model.classes_, proba)
    }
    # Present in a stable Low/Moderate/High order.
    confidence = {label: confidence[label] for label in ["Low", "Moderate", "High"]}

    factors = explain_prediction(engineered)
    recommendations = build_recommendations(factors)

    return {
        "financial_stress_level": class_mapping[predicted_class],
        "confidence": confidence,
        "contributing_factors": factors,
        "recommendations": recommendations,
        "disclaimer": (
            "This is an automated estimate based on spending patterns, not a "
            "financial or psychological diagnosis."
        ),
    }


@app.exception_handler(Exception)
async def handle_unexpected_error(request: Request, exc: Exception):
    # Last-resort safety net: any exception not already turned into a clean
    # HTTPException/validation response is logged server-side (with full
    # traceback) but the client only ever sees a generic message -- never a
    # file path, stack trace, or raw exception string.
    logger.exception("Unhandled error while processing %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "An internal error occurred. Please try again."})


# Mounted last (after /health and /predict are registered) so those routes
# keep precedence -- Starlette matches routes in registration order, and a
# mount at "/" would otherwise shadow them.
STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
