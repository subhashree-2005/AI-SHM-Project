from rest_framework.decorators import api_view

from rest_framework.response import Response

import joblib

# Load trained model
model = joblib.load("damage_model.pkl")


@api_view(['POST'])

def predict_damage(request):

    # Receive data
    frequency = request.data.get("frequency")

    rms = request.data.get("rms")

    # Prediction
    prediction = model.predict([[frequency, rms]])

    # Result
    if prediction[0] == 0:
        status = "Healthy"

    else:
        status = "Damaged"

    # Return response
    return Response({
        "frequency": frequency,
        "rms": rms,
        "status": status
    })