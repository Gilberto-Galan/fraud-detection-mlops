import xgboost as xgb
from src.utils import preprocess_data

class FraudPredictor:
    def __init__(self, model_path="models/fraud_model.json"):
        self.model = xgb.XGBClassifier()
        self.model.load_model(model_path)

    def predict(self, features_list):
        # Usamos la función de utils para que el trato sea consistente
        processed_features = preprocess_data(features_list)
        
        prediction = self.model.predict(processed_features)[0]
        probability = self.model.predict_proba(processed_features)[0][1]
        
        return {
            "is_fraud": bool(prediction),
            "probability": float(probability),
            "status": "High Risk" if prediction else "Safe"
        }