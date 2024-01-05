from keras.models import load_model
import joblib
import pandas as pd

model = load_model('model.h5')
scaler = joblib.load('minmax_scaler.pkl')


def generate(open, high, low, volume, days):
    response = []
    cur_open = open
    for _ in range(days):
        cur_open = float(model.predict(
            scaler.transform(
                pd.DataFrame(
                    [[cur_open, high, low, volume]],
                    columns=["Open", "High", "Low", "Volume"]
                )
            )
        )[0][0])
        response.append(cur_open)
    print(response)
    return response
