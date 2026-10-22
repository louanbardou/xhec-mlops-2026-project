import pandas as pd
from sklearn.model_selection import train_test_split

TARGET = "Rings"


def load_data(path: str) -> pd.DataFrame:
    """Read the csv and drop the rows with a height of 0 (errors found in the EDA)."""
    df = pd.read_csv(path)
    return df[df["Height"] > 0]


def split_data(df: pd.DataFrame) -> tuple:
    """Split into X_train, X_test, y_train, y_test (80/20)."""
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    return train_test_split(X, y, test_size=0.2, random_state=42)
