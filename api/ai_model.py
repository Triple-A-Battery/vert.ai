import numpy as np
import pandas as pd
from sklearn import tree

model = tree.DecisionTreeClassifier()


def train_model(data):
    global model
    new = data.rename({"Unnamed: 0": "a"}, axis="columns")
#     new = new[:10000]
    new.drop([
        #         "investment",
        "company",
        "sector",
        #         "horizon (days)",
        "Volatility_Buy",
        "Volatility_sell",
        "Sharpe Ratio",
        "inflation",
        "nominal_return",

        #         "PE_ratio",
        "EPS_ratio",
        "PS_ratio",
        "NetProfitMargin_ratio",
        "amount",
        #         "price_BUY",
        "price_SELL",
        "current_ratio",
        "date_BUY_fix",
        "date_SELL_fix",
        "a",
        "expected_return (yearly)",

        #         "ESG_ranking",
        "PB_ratio",
        "roa_ratio",
        #         "roe_ratio",
    ], axis=1, inplace=True)

    y_new = new['investment'].replace({"GOOD": 1, "BAD": 0})
    x_new = new.drop('investment', axis=1)

    np.random.seed(42)
    model = model.fit(x_new, y_new)


def generate_data(data):
    return model.predict(data)


data = pd.read_csv("./training_data.csv")
train_model(data)
