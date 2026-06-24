import firebase_admin

from firebase_admin import credentials

from firebase_admin import db

import joblib



# Load AI Model
model = joblib.load("damage_model.pkl")



# Firebase Secret Key
cred = credentials.Certificate(
    "ai-shm-project-firebase-adminsdk-fbsvc-60d188b3e3.json"
)



# Connect Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL':
    'https://ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
})



# Read cloud data
ref = db.reference('sensor_data')

data = ref.get()



# Loop through Firebase data
for key, value in data.items():

    frequency = value["frequency"]

    rms = value["rms"]


    prediction = model.predict(
        [[frequency, rms]]
    )


    if prediction[0] == 0:

        result = "Healthy"

    else:

        result = "Damaged"


    print("Frequency:", frequency)

    print("RMS:", rms)

    print("AI Prediction:", result)

    print("-------------------")