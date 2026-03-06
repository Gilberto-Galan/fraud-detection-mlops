from fastapi.testclient import TestClient
from api.main import app

# Creamos un cliente de prueba que "envuelve" nuestra API
client = TestClient(app)

def test_health_check():
    """Prueba que el servidor esté vivo y responda en la ruta raíz"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "model": "XGBoost v1"}

def test_predict_success():
    """Prueba que el modelo haga una predicción correcta con 10 datos"""
    payload = {
        "features": [0.1, 1.2, -0.5, 3.4, 0.0, 1.1, 0.9, -1.2, 0.4, 2.2]
    }
    response = client.post("/predict", json=payload)
    
    # Verificamos que responda con éxito (200 OK)
    assert response.status_code == 200
    
    # Verificamos que la respuesta tenga la estructura correcta
    data = response.json()
    assert "is_fraud" in data
    assert "probability" in data
    assert "status" in data

def test_predict_invalid_input():
    """Prueba que la API rechace datos incorrectos (ej. menos de 10 features)"""
    payload = {
        "features": [0.1, 1.2, -0.5] # Solo enviamos 3 números
    }
    response = client.post("/predict", json=payload)
    
    # Verificamos que responda con error de validación (400 Bad Request)
    assert response.status_code == 400
    assert response.json()["detail"] == "Se requieren 10 features"