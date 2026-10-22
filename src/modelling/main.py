# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from pathlib import Path

from src.modelling.preprocessing import load_data, split_data
from src.modelling.training import evaluate_model, train_model
from src.modelling.utils import pickle_object


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    df = load_data(trainset_path)
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    print("Test metrics:", evaluate_model(model, X_test, y_test))
    pickle_object(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
