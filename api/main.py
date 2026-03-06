from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.predict import FraudPredictor

app = FastAPI(title="Fraud Detection API")

# Instanciamos el predictor
predictor = FraudPredictor()

class TransactionData(BaseModel):
    features: list[float]

@app.get("/")
def health_check():
    return {"status": "online", "model": "XGBoost v1"}

@app.post("/predict")
def get_prediction(data: TransactionData):
    if len(data.features) != 10:
        raise HTTPException(status_code=400, detail="Se requieren 10 features")
    
    result = predictor.predict(data.features)
    return result