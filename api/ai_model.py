import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

import keras
from keras.regularizers import l1_l2


scaler = MinMaxScaler()


def get_data(data):
    new = data.rename({"Unnamed: 0": "a"}, axis="columns")
    new.drop(
        [
            "investment",
            "company",
            "sector",
            "Volatility_Buy",
            "Volatility_sell",
            "Sharpe Ratio",
            "inflation",
            "nominal_return",
            "EPS_ratio",
            "PS_ratio",
            "NetProfitMargin_ratio",
            "amount",
            "current_ratio",
            "date_BUY_fix",
            "date_SELL_fix",
            "a",
            "ESG_ranking",
            "roa_ratio",
            "roe_ratio",
        ],
        axis=1,
        inplace=True,
    )

    new = pd.DataFrame(scaler.fit_transform(new), columns=new.columns)
    y_new = new["price_SELL"]
    x_new = new.drop("price_SELL", axis=1)
    return x_new, y_new


def generate_data(data):
    x_train, y_train = get_data(data)
    np.random.seed(42)

    model = keras.Sequential(
        [
            keras.layers.Dense(32, activation="linear", input_dim=x_train.shape[1]),
            keras.layers.Dense(64, activation="tanh", input_dim=x_train.shape[1]),
            keras.layers.Dropout(0.1),
            keras.layers.Dense(32, activation="tanh", input_dim=x_train.shape[1]),
            keras.layers.Dropout(0.1),
            key_pred = scaler.inverse_transform(model.predict(x_train[start:start+n]))ras.layers.Dense(1, activation="linear"),
        ]
    )

    model.compile(
        loss="mae",
        optimizer=keras.optimizers.Adam(learning_rate=0.0001),
        metrics=["mae"],
    )
    training = model.fit(
        x_train[0:], y_train[0:], batch_size=32, epochs=1, validation_split=0.1
    )

    start = 0
    n = 100
    y_pred = scaler.inverse_transform(model.predict(x_train[start : start + n]))
    y_pred = pd.DataFrame(
        (y_pred - x_train["price_BUY"][start : start + n].to_numpy() > 0)
        .astype(int)
        .ravel(),
        columns=["investment"],
    )
    y_test = pd.DataFrame(
        data["investment"].replace({"GOOD": 1, "BAD": 0})[0:]
    ).reset_index(drop=True)

    return y_test
