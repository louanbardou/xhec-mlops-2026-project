import pandas as pd

from src.modelling.preprocessing import load_data, split_data
from src.modelling.training import evaluate_model, train_model


def test_train_and_evaluate():
    df = load_data("data/abalone.csv")
    assert (df["Height"] > 0).all()

    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)

    assert evaluate_model(model, X_test, y_test)["rmse"] < 3
    assert len(model.predict(pd.DataFrame(X_test.head(2)))) == 2
