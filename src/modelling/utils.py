import pickle
from pathlib import Path

MODEL_PATH = Path("src/web_service/local_objects/model.pkl")


def pickle_object(obj: object, path: Path = MODEL_PATH) -> None:
    """Save an object (the model pipeline) in a pickle file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: Path = MODEL_PATH) -> object:
    """Load an object from a pickle file."""
    with open(path, "rb") as f:
        return pickle.load(f)
