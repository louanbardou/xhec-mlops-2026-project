import json
import pickle
from datetime import datetime
from pathlib import Path

# Where the trained model is saved. The API reads it from the same place
MODEL_PATH = Path("src/web_service/local_objects/model.pkl")
# One line per training run (date + metrics), the dashboard reads it
METRICS_PATH = Path("src/web_service/local_objects/metrics.jsonl")


def pickle_object(obj: object, path: Path = MODEL_PATH) -> None:
    """Save an object (the model pipeline) in a pickle file."""
    # Create the folder if it doesn't exist yet
    path.parent.mkdir(parents=True, exist_ok=True)
    # "wb" = write in binary, pickle turns the python object into bytes
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: Path = MODEL_PATH) -> object:
    """Load an object from a pickle file."""
    # "rb" = read in binary, pickle rebuilds the python object from the bytes
    with open(path, "rb") as f:
        return pickle.load(f)


def log_metrics(metrics: dict, path: Path = METRICS_PATH) -> None:
    """Add the metrics of this training run at the end of a jsonl file (one json per line)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # "a" = append, so we keep the history of all the trainings
    with open(path, "a") as f:
        row = {"date": datetime.now().isoformat(timespec="seconds"), **metrics}
        f.write(json.dumps(row) + "\n")
