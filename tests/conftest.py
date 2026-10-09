import sys
from pathlib import Path

import pandas as pd
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from fastapi.testclient import TestClient  # noqa: E402

from scripts.validate_api import row_to_payload  # noqa: E402
from src.app.api import app  # noqa: E402

CLEANED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="session")
def cleaned_df():
    return pd.read_csv(CLEANED_PATH).set_index("user_id")


@pytest.fixture
def valid_payload(cleaned_df):
    """A complete, valid /predict request payload built from a real
    (already-cleaned) user record, so it's grounded in genuine data
    rather than hand-invented numbers."""
    return row_to_payload(cleaned_df.loc["U100000"])
