import json
from sklearn.ensemble import RandomForestRegressor
import joblib

with open("../data/dataset.json") as f:
    data = json.load(f)

X = []
y = []

for d in data:
    X.append([
        d["users"],
        d["required_iops"],
        d["required_throughput_mb"],
        d["latency_target_ms"]
    ])
    y.append(d["disk_count"])

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model trained")