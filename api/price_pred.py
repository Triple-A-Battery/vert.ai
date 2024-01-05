from keras.models import load_model
import joblib
import pandas as pd
import random

model = load_model('model.h5')
scaler = joblib.load('minmax_scaler.pkl')


def generate(open, high, low, volume, days):
    random.seed(open)
    response = []
    cur_open = open
    for _ in range(days):
        cur_open = float(model.predict(
            scaler.transform(
                pd.DataFrame(
                    # Seeded random
                    [[cur_open, high + random.random() * (cur_open - open),
                      low + random.random() * (cur_open - open), volume]],
                    columns=["Open", "High", "Low", "Volume"]
                )
            )
        )[0][0])
        response.append(cur_open)
    print(response)
    return response
