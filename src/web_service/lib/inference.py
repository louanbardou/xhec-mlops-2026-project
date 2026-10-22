from functools import lru_cache

import pandas as pd

from src.modelling.predicting import predict
from src.modelling.utils import load_pickle
from src.web_service.lib.models import AbaloneInput, PredictionOutput

# API field name -> column name in the dataset (the model was trained with these names)
COLUMNS = {
    "sex": "Sex",
    "length": "Length",
    "diameter": "Diameter",
    "height": "Height",
    "whole_weight": "Whole weight",
    "shucked_weight": "Shucked weight",
    "viscera_weight": "Viscera weight",
    "shell_weight": "Shell weight",
}


@lru_cache
def get_model():
    """Load the model once (raises FileNotFoundError if the model was not trained)."""
    return load_pickle()


def run_inference(abalone: AbaloneInput) -> PredictionOutput:
    """Predict the rings and the age of one abalone."""
    data = pd.DataFrame([abalone.model_dump()]).rename(columns=COLUMNS)
    rings = predict(get_model(), data)[0]
    return PredictionOutput(rings=rings, age=rings + 1.5)
