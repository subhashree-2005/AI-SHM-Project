import firebase_admin

from firebase_admin import credentials

from firebase_admin import db


# Firebase secret key file
cred = credentials.Certificate(
    "ai-shm-project-firebase-adminsdk-fbsvc-60d188b3e3.json"
)

# Initialize Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL':
    'https://ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

print("Firebase Connected Successfully!")
# Create database reference
ref = db.reference('sensor_data')

# Upload sample data
ref.push({

    "frequency": 16,

    "rms": 0.6,

    "status": "Damaged"
})

print("Data Uploaded Successfully!")