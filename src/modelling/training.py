import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """Train a linear regression, with Sex one-hot encoded (the encoder is inside the pipeline)."""
    pipeline = Pipeline(
        [
            (
                "encode",
                ColumnTransformer([("sex", OneHotEncoder(), ["Sex"])], remainder="passthrough"),
            ),
            ("model", LinearRegression()),
        ]
    )
    return pipeline.fit(X_train, y_train)


def evaluate_model(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Return the RMSE and the MAE on the test set."""
    pred = model.predict(X_test)
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_test, pred))),
        "mae": float(mean_absolute_error(y_test, pred)),
    }
