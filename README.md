# Intelligent Financial Stress Detection System

An academic dissertation prototype that classifies users into Low / Moderate / High
financial stress from spending-behavior data, using machine learning, exposed
through a FastAPI backend and a calm, non-clinical single-page frontend
("Financial Weather" — Clear / Changeable / Stormy).

See [`docs/research_proposal_.docx`](docs/research_proposal_.docx) for the
full research proposal and [`docs/data_dictionary.md`](docs/data_dictionary.md)
for the dataset's column definitions and labeling methodology.

## Prerequisites

- **Python 3.14** (developed and tested against `Python 3.14.0`; Python 3.11+
  should work, but 3.14 is the only version this has been verified against —
  see Troubleshooting below if you're on an older version).
- No Node.js or other runtime required to *run* the app — the frontend is
  plain HTML/CSS/JS with no build step. Node is only used optionally by the
  frontend self-check script (`scripts/validate_frontend.py`) to lint the JS.

## Setup

From the project root:

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (Git Bash):
source venv/Scripts/activate
# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies (pinned, see requirements.txt)
pip install -r requirements.txt
```

`requirements.txt` includes everything needed to run the API. It also
includes a clearly-marked dev-only section (`pytest`, `playwright`,
`httpx`, `requests`) used by the test suite and the `scripts/validate_*.py`
self-checks — not required just to run the app.

## Running the app

```bash
python -m uvicorn src.app.api:app --host 127.0.0.1 --port 8000
```

Then open **http://127.0.0.1:8000** in a browser — this serves the
frontend directly (mounted via FastAPI's `StaticFiles`) and it calls the
`/predict` API on the same origin. No separate frontend server needed.

Other useful endpoints:
- `GET /health` — `{"status": "ok", "model_loaded": true}` when the model
  loaded successfully.
- `POST /predict` — the prediction endpoint the frontend calls; see
  [`docs/user_guide.md`](docs/user_guide.md) for what the response means,
  or read `src/app/api.py`'s docstring for the technical contract.
- `GET /docs` — FastAPI's interactive Swagger UI for the API.

Add `--reload` during development to auto-restart on file changes.

## Running the tests

```bash
python -m pytest tests/ -v
```

Covers: ratio-feature unit tests (including the zero-income/zero-expenditure
guard), a full-pipeline functional test, ~46 API input-validation/security
cases, and a basic performance check. See `tests/` for details.

Additional one-off validation scripts (used while building each stage of
the pipeline, safe to re-run any time) live in `scripts/`:
`validate_dataset.py`, `validate_cleaning.py`, `validate_features.py`,
`validate_modeling.py`, `validate_api.py`, `validate_frontend.py`.

## Project structure

```
financial-stress-detection/
├── data/
│   ├── raw/                 synthetic_financial_data.csv (source dataset)
│   ├── processed/           cleaned_data.csv, engineered feature CSVs
│   └── interim/             (reserved for intermediate outputs)
├── docs/
│   ├── research_proposal_.docx
│   ├── data_dictionary.md   column definitions + labeling methodology
│   └── user_guide.md        end-user guide for the app
├── models/                  trained model artifacts (.joblib) + metadata
├── notebooks/                (reserved for exploratory analysis)
├── reports/
│   ├── figures/              charts, SHAP plots, frontend screenshots
│   └── results/               model comparison table, selection writeup,
│                               data cleaning log
├── scripts/                  one-off / re-runnable pipeline + validation scripts
├── src/
│   ├── app/
│   │   ├── api.py            FastAPI backend (/predict, /health)
│   │   └── static/            frontend (index.html, style.css, app.js)
│   ├── data/                  cleaning + train/test split
│   ├── features/              feature engineering (ratios, encoding, scaling)
│   ├── models/                model training + selection
│   ├── evaluation/             evaluation, SHAP explainability, explain_prediction()
│   └── utils.py                shared constants (feature column list, class names)
├── tests/                     pytest suite
└── requirements.txt
```

## Troubleshooting

**"Port 8000 already in use" / `[Errno 98] Address already in use`**
Another process is already listening on that port (maybe a previous run of
this same server). Either stop it, or run on a different port:
`python -m uvicorn src.app.api:app --host 127.0.0.1 --port 8001` (then open
`http://127.0.0.1:8001` instead).

**Python version mismatch (`SyntaxError` on startup, or `pip install` failing
to find a compatible wheel for a pinned package)**
This project was built and verified against Python 3.14.0. If you're on an
older Python (e.g. 3.9), some pinned versions in `requirements.txt` may not
have wheels available for your interpreter. Either install Python 3.14, or
try `pip install -r requirements.txt` without version pins and expect minor
behavior differences.

**`GET /health` returns `model_loaded: false`, or `/predict` returns
`503 Model is not currently available`**
The model artifacts under `models/` (`best_model.joblib`,
`best_model_metadata.json`, `scaler.joblib`) failed to load — most likely
the `models/` directory wasn't copied over, or a package version mismatch
means a `.joblib` file pickled with a different scikit-learn/xgboost version
can't be unpickled. Confirm the `models/` folder exists with all `.joblib`
files, and that `pip list` matches the pinned versions in `requirements.txt`.

**`ModuleNotFoundError` for something not in `requirements.txt`**
Check whether the missing package is one of the dev-only entries (`pytest`,
`playwright`, `httpx`, `requests`) — those are only needed for
`pytest tests/` and the `scripts/validate_*.py` self-checks, not for running
the app itself.
