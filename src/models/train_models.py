"""Train and cross-validate the 5 candidate financial stress classifiers.

Logistic Regression and SVM train on features_scaled.csv (train split).
Decision Tree, Random Forest, and XGBoost train on features_unscaled.csv
(train split). All five use financial_stress_level_encoded as the target
and random_state=42. Each model is 5-fold stratified cross-validated on
the training set (F1-macro reported as mean +/- std), then refit on the
full training set and saved to models/*.joblib.
"""
import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.utils import REPO_ROOT, TARGET_COLUMN, get_feature_columns  # noqa: E402

UNSCALED_PATH = REPO_ROOT / "data" / "processed" / "features_unscaled.csv"
SCALED_PATH = REPO_ROOT / "data" / "processed" / "features_scaled.csv"
MODELS_DIR = REPO_ROOT / "models"

RANDOM_STATE = 42
CV_FOLDS = 5


def cross_validate(model, X, y, label):
    cv = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    scores = cross_val_score(model, X, y, cv=cv, scoring="f1_macro")
    print(f"{label}: CV F1-macro = {scores.mean():.4f} +/- {scores.std():.4f} (folds={scores.tolist()})")
    return scores


def main():
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    unscaled_df = pd.read_csv(UNSCALED_PATH)
    scaled_df = pd.read_csv(SCALED_PATH)

    unscaled_train = unscaled_df[unscaled_df["split"] == "train"].reset_index(drop=True)
    scaled_train = scaled_df[scaled_df["split"] == "train"].reset_index(drop=True)

    unscaled_features = get_feature_columns(unscaled_df)
    scaled_features = get_feature_columns(scaled_df)
    assert unscaled_features == scaled_features, "Feature column sets/order must match between files"

    X_unscaled = unscaled_train[unscaled_features]
    y_unscaled = unscaled_train[TARGET_COLUMN]
    X_scaled = scaled_train[scaled_features]
    y_scaled = scaled_train[TARGET_COLUMN]

    assert list(unscaled_train["user_id"]) == list(scaled_train["user_id"]), (
        "Train rows must be identical (same order) across both feature files"
    )

    models = {
        "logreg": (
            LogisticRegression(max_iter=2000, random_state=RANDOM_STATE),
            X_scaled, y_scaled,
        ),
        "svm": (
            SVC(kernel="rbf", probability=True, random_state=RANDOM_STATE),
            X_scaled, y_scaled,
        ),
        "decision_tree": (
            DecisionTreeClassifier(random_state=RANDOM_STATE),
            X_unscaled, y_unscaled,
        ),
        "random_forest": (
            RandomForestClassifier(n_estimators=300, random_state=RANDOM_STATE),
            X_unscaled, y_unscaled,
        ),
        "xgboost": (
            XGBClassifier(
                objective="multi:softprob",
                num_class=3,
                eval_metric="mlogloss",
                random_state=RANDOM_STATE,
            ),
            X_unscaled, y_unscaled,
        ),
    }

    print(f"Training feature columns ({len(unscaled_features)}): {unscaled_features}")
    print()

    for name, (model, X, y) in models.items():
        cross_validate(model, X, y, name)
        model.fit(X, y)
        out_path = MODELS_DIR / f"{name}.joblib"
        joblib.dump(model, out_path)
        print(f"  saved -> {out_path}")
        print()


if __name__ == "__main__":
    main()
