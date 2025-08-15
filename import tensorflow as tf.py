import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

# Load pre-trained behavior analysis model
model = load_model('behavior_model.h5')

def authenticate_user(username, password, metadata):
    # Verify basic credentials (mock database check)
    if not verify_credentials(username, password):
        return False

    # Extract features from metadata (e.g., typing speed, device, location)
    features = extract_features(metadata)
    features = np.array([features])  # Reshape for model input

    # Predict risk score using AI model
    risk_score = model.predict(features)[0][0]

    # Adaptive authentication decision
    if risk_score < 0.2:  # Low risk: allow login
        return True
    elif risk_score < 0.8:  # Medium risk: require MFA
        return request_mfa(username)
    else:  # High risk: block login
        return False

# Mock functions for demonstration
def verify_credentials(username, password):
    return username == "user" and password == "pass"

def extract_features(metadata):
    return [metadata['typing_speed'], metadata['location_anomaly']]

def request_mfa(username):
    print(f"MFA required for {username}")
    return input("Enter MFA code: ") == "123456"

# Example usage
metadata = {'typing_speed': 0.8, 'location_anomaly': 0}
print(authenticate_user("user", "pass", metadata))