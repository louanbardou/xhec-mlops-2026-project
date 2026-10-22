import pandas as pd
from sklearn.pipeline import Pipeline


def predict(model: Pipeline, data: pd.DataFrame) -> list[float]:
    """Predict the number of rings for new abalones."""
    return model.predict(data).tolist()
