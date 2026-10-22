import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """Train a linear regression, with Sex one-hot encoded (the encoder is inside the pipeline)."""
    # A pipeline chains the steps: first the encoding, then the model
    # Putting both in one object means the API applies the same encoding as in training
    pipeline = Pipeline(
        [
            (
                "encode",
                # Sex is text (M, F, I) and the model needs numbers, so we turn it into 0/1 columns
                # remainder="passthrough" keeps the other columns (already numbers) as they are
                ColumnTransformer([("sex", OneHotEncoder(), ["Sex"])], remainder="passthrough"),
            ),
            # Simple model, it was as good as the random forest in the notebook
            ("model", LinearRegression()),
        ]
    )
    # fit = the model learns from the training data
    return pipeline.fit(X_train, y_train)


def evaluate_model(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Return the RMSE and the MAE on the test set."""
    # Predict on data the model never saw, then compare with the real number of rings
    pred = model.predict(X_test)
    return {
        # RMSE: typical error in rings (big mistakes count more)
        "rmse": float(np.sqrt(mean_squared_error(y_test, pred))),
        # MAE: average error in rings
        "mae": float(mean_absolute_error(y_test, pred)),
    }
