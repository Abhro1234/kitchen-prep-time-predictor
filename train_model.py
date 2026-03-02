import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor

np.random.seed(42)

X = []
y = []

for i in range(500):

    orders = np.random.randint(1, 20)
    avg_prep = np.random.randint(10, 25)
    peak = np.random.randint(0, 2)
    weekend = np.random.randint(0, 2)

    prep_time = (
        avg_prep
        + orders * 1.5
        + peak * 5
        + weekend * 3
        + np.random.normal(0, 2)
    )

    X.append([orders, avg_prep, peak, weekend])
    y.append(prep_time)

model = RandomForestRegressor()
model.fit(X, y)

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/prep_time_model.pkl")

print("Model trained successfully")