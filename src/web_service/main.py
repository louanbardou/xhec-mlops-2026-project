# Code with FastAPI (app = FastAPI(...))

from fastapi import FastAPI, HTTPException

from src.web_service.lib.inference import run_inference
from src.web_service.lib.models import AbaloneInput, PredictionOutput

app = FastAPI(
    title="Abalone age prediction",
    description="Predicts the number of rings (and the age) of an abalone from its measurements.",
)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOutput, status_code=201)
def predict(payload: AbaloneInput) -> PredictionOutput:
    try:
        return run_inference(payload)
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model not found, run `make train` first.")
