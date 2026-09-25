import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):
    return pd.read_csv(path)


def preprocess_data(df, features):
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df, scaler


if __name__ == "__main__":
    features = ["sensor_1", "sensor_2", "sensor_3", "sensor_4"]

    df = load_data("data/sample/sensor_sample.csv")
    df, scaler = preprocess_data(df, features)

    print(df.head())
