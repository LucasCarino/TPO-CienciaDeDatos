import joblib

def load_model_and_features(model_path, features_path):
    best_model = joblib.load(model_path)
    features = joblib.load(features_path)
    return best_model, features
