from fuzzywuzzy import process

def get_user_symptoms(features):
    """Solicita al usuario que ingrese síntomas y selecciona los más cercanos del diccionario hasta que escriba -1."""
    print("Ingrese síntomas para hacer una predicción. Escriba -1 para finalizar.")
    user_symptoms = []
    
    while True:
        symptom = input(f"Ingrese el síntoma {len(user_symptoms) + 1}: ").strip().lower()
        if symptom == '-1':
            break
        
        suggested_symptoms = process.extract(symptom, features, limit=3)
        print("Síntomas sugeridos:")
        for i, (s, score) in enumerate(suggested_symptoms):
            print(f"{i + 1}. {s} (confianza: {score}%)")
        
        choice = int(input("Seleccione el síntoma correcto (1-3) o 0 para ingresar de nuevo: "))
        if 1 <= choice <= 3:
            selected_symptom = suggested_symptoms[choice - 1][0]
            user_symptoms.append(selected_symptom)
            print(f"Síntoma agregado: {selected_symptom}")
        else:
            print("Por favor, vuelva a intentar con un nuevo síntoma.")
    
    return user_symptoms
