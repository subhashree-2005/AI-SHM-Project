import firebase_admin

from firebase_admin import credentials

from firebase_admin import db


# Firebase secret key
cred = credentials.Certificate(
    "ai-shm-project-firebase-adminsdk-fbsvc-60d188b3e3.json"
)

# Connect Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL':
    'https://ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


# Read sensor data
ref = db.reference('sensor_data')

data = ref.get()

print(data)