import pandas as pd

from src.modelling.utils import load_pickle


def predict(data: pd.DataFrame) -> list[float]:
    """Predict the number of rings for new abalones with the saved model."""
    model = load_pickle()
    return model.predict(data).tolist()
