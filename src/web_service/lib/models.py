# Pydantic models for the web service

from typing import Literal

from pydantic import BaseModel, Field


class AbaloneInput(BaseModel):
    """Measurements of one abalone (same columns as the dataset)."""

    sex: Literal["M", "F", "I"]
    length: float = Field(gt=0)
    diameter: float = Field(gt=0)
    height: float = Field(gt=0)
    whole_weight: float = Field(gt=0)
    shucked_weight: float = Field(gt=0)
    viscera_weight: float = Field(gt=0)
    shell_weight: float = Field(gt=0)


class PredictionOutput(BaseModel):
    """Predicted number of rings, and the age (rings + 1.5)."""

    rings: float
    age: float
