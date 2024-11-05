import numpy as np

def prepare_input(symptoms_list, features):
    """Convierte la lista de síntomas en una matriz binaria de entrada."""
    input_vector = np.zeros(len(features))
    
    for symptom in symptoms_list:
        if symptom in features:
            index = features.index(symptom)
            input_vector[index] = 1
        else:
            print(f"Síntoma '{symptom}' no encontrado en las características del modelo.")
    
    input_vector = input_vector.reshape(1, -1)
    return input_vector
