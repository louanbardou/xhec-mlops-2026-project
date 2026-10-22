import pandas as pd
from sklearn.pipeline import Pipeline


def predict(model: Pipeline, data: pd.DataFrame) -> list[float]:
    """Predict the number of rings for new abalones."""
    # data needs the same columns as in training (the pipeline encodes Sex by itself)
    # tolist() gives a normal python list instead of a numpy array
    return model.predict(data).tolist()
