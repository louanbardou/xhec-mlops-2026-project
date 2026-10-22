# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from pathlib import Path

from prefect import flow, task

from src.modelling.preprocessing import load_data, split_data
from src.modelling.training import evaluate_model, train_model
from src.modelling.utils import pickle_object

load_data_task = task(load_data)
split_data_task = task(split_data)
train_model_task = task(train_model)
evaluate_model_task = task(evaluate_model)
pickle_object_task = task(pickle_object)


@flow(name="train-abalone-model", log_prints=True)
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    df = load_data_task(trainset_path)
    X_train, X_test, y_train, y_test = split_data_task(df)
    model = train_model_task(X_train, y_train)
    print("Test metrics:", evaluate_model_task(model, X_test, y_test))
    pickle_object_task(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
