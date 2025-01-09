import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


def predict_future(filepath='./data/raw_data.csv', model_path='./models/lstm_model.h5', look_back=60):
    model = load_model(model_path)
    data = pd.read_csv(filepath)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Exchange_Rate'].values.reshape(-1, 1))

    test_data = scaled_data[-look_back:]
    X_test = [test_data]
    X_test = np.array(X_test)
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    prediction = model.predict(X_test)
    prediction = scaler.inverse_transform(prediction)

    print(f"Gelecek tahmin: {prediction.flatten()[0]}")
    return prediction.flatten()[0]


if __name__ == "__main__":
    predict_future()
