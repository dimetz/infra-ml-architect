from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("../../models/model.pkl")

@app.get("/")
def root():
    return {"status": "infra-ml running"}

@app.post("/predict")
def predict(data: dict):
    features = [[
        data["users"],
        data["iops"],
        data["throughput"],
        data["latency"]
    ]]

    disks = int(model.predict(features)[0])

    return {
        "recommended_disks": disks,
        "note": "ML estimation"
    }