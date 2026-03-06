import pandas as pd
import numpy as np

def preprocess_data(data):
    """
    Simula la limpieza de datos. 
    En un caso real aquí manejarías valores nulos o escalado.
    """
    # Convertimos a array de numpy si es una lista
    features = np.array(data).reshape(1, -1)
    return features

def logger_info(message):
    print(f"[INFO] {message}")