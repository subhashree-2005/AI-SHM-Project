import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import random
import time
import joblib

cred = credentials.Certificate("firebase_key.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(
        cred,
        {
            'databaseURL':
            'https://ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
        }
    )

ref = db.reference('sensor_data')

model = joblib.load("advanced_damage_model.pkl")

print("Live Sensor Started...")

while True:

    frequency = round(random.uniform(10, 80), 2)

    rms = round(random.uniform(0.1, 3.5), 2)

    prediction = model.predict([[frequency, rms]])

    if prediction[0] == 1:
        status = "Damaged"
    else:
        status = "Healthy"

    ref.push({
        "frequency": frequency,
        "rms": rms,
        "status": status
    })

    print(
        f"Sent -> Frequency: {frequency}, RMS: {rms}, Status: {status}"
    )

    time.sleep(5)