import numpy as np
from src.prepare_input import prepare_input

def predict_disease(best_model, symptoms_list, features):
    """Realiza la predicción de la enfermedad basada en los síntomas confirmados del usuario."""
    entrada_reducida = prepare_input(symptoms_list, features)
    predictions = best_model.predict_proba(entrada_reducida)

    top_n = 3  # Mostrar las 3 predicciones más probables
    top_indices = np.argsort(predictions[0])[-top_n:][::-1]
    for idx in top_indices:
        disease_name = best_model.classes_[idx]  # Obtener el nombre de la enfermedad
        probability = predictions[0][idx]
        print(f"Enfermedad: {disease_name}, Probabilidad: {probability:.2%}")
