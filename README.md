# 🛡️ Real-Time Fraud Detection MLOps System

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)](https://fastapi.tiangolo.com/)
[![MLflow](https://img.shields.io/badge/MLflow-2.10.0-blue.svg)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)

Sistema profesional de detección de fraude bancario diseñado con una arquitectura **MLOps** de extremo a extremo. Este proyecto demuestra la integración de modelos de Machine Learning en entornos de producción, garantizando reproducibilidad, observabilidad y escalabilidad.

---

# 🚀 Características del Proyecto
* **Arquitectura Modular (Clean Code):** Separación estricta entre entrenamiento (`src/train.py`), lógica de inferencia (`src/predict.py`) y servicio web (`api/main.py`).
* **Tracking de Experimentos:** Gestión completa del ciclo de vida del modelo con **MLflow**, registrando hiperparámetros y métricas como F1-Score y Precision-Recall.
* **Inferencia de Baja Latencia:** Implementación con **XGBoost** y **FastAPI**, optimizada para procesamiento en tiempo real.
* **Contenedores de Grado de Producción:** Configuración con **Docker** y **Docker Compose** para un despliegue agnóstico al entorno.
* **Validación de Esquemas:** Uso de **Pydantic** para garantizar la integridad de los datos de entrada.

---

# 🛠️ Instalación y Ejecución

### Clonar el repositorio

`git clone https://github.com/tu-usuario/fraud-detection-mlops.git`

`cd fraud-detection-mlops`

### Crear entorno virtual
`python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
`

### Instalar dependencias con versiones fijas para evitar conflictos
`pip install -r requirements.txt `

### Ciclo de Entrenamiento
El script genera automáticamente un dataset de prueba si no existe y registra el experimento:

`python src/train.py`

### Despliegue con Docker (API + UI)
La forma más robusta de ejecutar el sistema completo:

`docker-compose up --build`

`Swagger UI (API Docs): http://localhost:8000/docs`

`MLflow Dashboard: http://localhost:5000`

# 🧪 Testing y Validación
Garantizamos la estabilidad del sistema mediante pruebas automáticas:

### Ejecutar tests unitarios
`pytest tests/`

### Prueba de predicción manual (CURL)
```curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{ "features": [0.5, -1.2, 3.4, 0.1, 0.9, -0.4, 1.1, 2.2, -0.1, 0.5] }'```