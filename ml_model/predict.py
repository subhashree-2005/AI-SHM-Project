import joblib

# Load trained model
model = joblib.load("damage_model.pkl")

# Example new vibration data
frequency = 20
rms = 0.4

# Prediction
prediction = model.predict([[frequency, rms]])

# Output
if prediction[0] == 0:
    print("Structure is Healthy")

else:
    print("Structure is Damaged")