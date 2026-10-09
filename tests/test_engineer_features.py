"""Unit tests for the 7 ratio functions in src/features/engineer_features.py."""
import math

import pandas as pd
import pytest

from src.features.engineer_features import RATIO_FEATURE_COLUMNS, engineer_ratio_features


def make_row(**overrides):
    row = {
        "monthly_income": 10000.0,
        "monthly_expenditure": 5000.0,
        "savings": 2000.0,
        "debt_repayment": 1000.0,
        "non_essential_expenditure": 2000.0,
        "essential_expenditure": 3000.0,
        "subscription_expenditure": 500.0,
        "spending_volatility": 1000.0,
    }
    row.update(overrides)
    return row


class TestKnownValues:
    def test_spending_to_income_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["spending_to_income_ratio"].iloc[0] == pytest.approx(5000.0 / 10000.0)

    def test_savings_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["savings_ratio"].iloc[0] == pytest.approx(2000.0 / 10000.0)

    def test_debt_to_income_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["debt_to_income_ratio"].iloc[0] == pytest.approx(1000.0 / 10000.0)

    def test_discretionary_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["discretionary_ratio"].iloc[0] == pytest.approx(2000.0 / 5000.0)

    def test_essential_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["essential_ratio"].iloc[0] == pytest.approx(3000.0 / 5000.0)

    def test_subscription_burden(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["subscription_burden"].iloc[0] == pytest.approx(500.0 / 10000.0)

    def test_spending_volatility_ratio(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        assert df["spending_volatility_ratio"].iloc[0] == pytest.approx(1000.0 / 10000.0)

    def test_negative_savings_produces_negative_savings_ratio(self):
        # Deficit spending (savings < 0) is a valid, documented case (see
        # data_dictionary.md) -- must not be clipped or errored on.
        df = engineer_ratio_features(pd.DataFrame([make_row(savings=-500.0)]))
        assert df["savings_ratio"].iloc[0] == pytest.approx(-500.0 / 10000.0)

    def test_all_seven_columns_produced(self):
        df = engineer_ratio_features(pd.DataFrame([make_row()]))
        for col in RATIO_FEATURE_COLUMNS:
            assert col in df.columns
            assert math.isfinite(df[col].iloc[0])


class TestZeroIncomeAndExpenditureGuard:
    """monthly_income / monthly_expenditure are ratio denominators. Division
    by zero is mathematically undefined -- pandas float division does NOT
    raise (0/0 -> NaN, nonzero/0 -> inf), so engineer_ratio_features adds an
    explicit guard that raises ValueError instead of letting NaN/inf silently
    reach the scaler or model. This test suite confirms that guard exists
    and behaves as documented."""

    def test_zero_income_raises_value_error(self):
        with pytest.raises(ValueError, match="monthly_income"):
            engineer_ratio_features(pd.DataFrame([make_row(monthly_income=0.0)]))

    def test_negative_income_raises_value_error(self):
        with pytest.raises(ValueError, match="monthly_income"):
            engineer_ratio_features(pd.DataFrame([make_row(monthly_income=-100.0)]))

    def test_zero_expenditure_raises_value_error(self):
        with pytest.raises(ValueError, match="monthly_expenditure"):
            engineer_ratio_features(pd.DataFrame([make_row(monthly_expenditure=0.0)]))

    def test_negative_expenditure_raises_value_error(self):
        with pytest.raises(ValueError, match="monthly_expenditure"):
            engineer_ratio_features(pd.DataFrame([make_row(monthly_expenditure=-1.0)]))

    def test_near_zero_income_does_not_crash_and_is_finite(self):
        # Near-zero (but not exactly zero) is mathematically well-defined,
        # just produces a large ratio -- this must NOT raise.
        df = engineer_ratio_features(pd.DataFrame([make_row(monthly_income=0.01)]))
        assert math.isfinite(df["spending_to_income_ratio"].iloc[0])
        assert df["spending_to_income_ratio"].iloc[0] == pytest.approx(5000.0 / 0.01)

    def test_near_zero_expenditure_does_not_crash_and_is_finite(self):
        df = engineer_ratio_features(pd.DataFrame([make_row(monthly_expenditure=0.01)]))
        assert math.isfinite(df["discretionary_ratio"].iloc[0])
        assert df["discretionary_ratio"].iloc[0] == pytest.approx(2000.0 / 0.01)

    def test_guard_checks_every_row_in_a_batch(self):
        # One bad row among otherwise-valid rows should still be caught.
        rows = [make_row(), make_row(monthly_income=0.0), make_row()]
        with pytest.raises(ValueError, match="monthly_income"):
            engineer_ratio_features(pd.DataFrame(rows))
