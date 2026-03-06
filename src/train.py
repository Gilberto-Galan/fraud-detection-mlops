import xgboost as xgb
import mlflow
import mlflow.xgboost
import os
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from utils import preprocess_data, logger_info

def run_training():
    logger_info("Iniciando generación de datos...")
    X, y = make_classification(n_samples=1000, n_features=10, weights=[0.95, 0.05], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    mlflow.set_experiment("Fraud_Detection_System")

    with mlflow.start_run():
        logger_info("Entrenando modelo XGBoost...")
        model = xgb.XGBClassifier(scale_pos_weight=19)
        model.fit(X_train, y_train)

        # Guardar localmente
        if not os.path.exists("models"):
            os.makedirs("models")
        model.save_model("models/fraud_model.json")
        
        # Registrar en MLflow
        mlflow.log_param("model_type", "XGBoost")
        mlflow.xgboost.log_model(model, "model")
        logger_info("Modelo guardado en models/fraud_model.json y registrado en MLflow")

if __name__ == "__main__":
    run_training()