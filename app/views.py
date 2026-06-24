from django.shortcuts import render
from django.http import JsonResponse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import joblib

from .models import SensorData
from .report_generator import generate_report


# ======================================
# FIREBASE CONNECTION
# ======================================

cred = credentials.Certificate(
    "firebase_key.json"
)

if not firebase_admin._apps:

    firebase_admin.initialize_app(
        cred,
        {
            'databaseURL':
            'https://ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
        }
    )


# ======================================
# LOAD AI MODEL
# ======================================

model = joblib.load(
    "advanced_damage_model.pkl"
)


# ======================================
# HOME PAGE
# ======================================

def home(request):

    return render(
        request,
        'index.html'
    )


# ======================================
# PROJECTS PAGE
# ======================================

def projects(request):

    return render(
        request,
        'projects.html'
    )


# ======================================
# CONTACT PAGE
# ======================================

def contact(request):

    return render(
        request,
        'contact.html'
    )


# ======================================
# DASHBOARD PAGE
# ======================================

def dashboard(request):

    ref = db.reference('sensor_data')

    data = ref.get()

    if data:

        latest_key = list(data.keys())[-1]

        latest = data[latest_key]

        frequency = latest.get(
            "frequency",
            0
        )

        rms = latest.get(
            "rms",
            0
        )

        status = latest.get(
            "status",
            "Unknown"
        )

        ax = latest.get(
            "ax",
            0
        )

        ay = latest.get(
            "ay",
            0
        )

        az = latest.get(
            "az",
            0
        )

    else:

        frequency = 0

        rms = 0

        status = "No Data"

        ax = 0

        ay = 0

        az = 0

    # Severity Logic

    if rms < 0.5:

        severity = "LOW"

        risk = "SAFE"

    elif rms < 1.5:

        severity = "MEDIUM"

        risk = "WARNING"

    elif rms < 3:

        severity = "HIGH"

        risk = "DANGER"

    else:

        severity = "CRITICAL"

        risk = "CRITICAL"

    # Problem Analysis

    if status == "Damaged":

        problem = (
            "Abnormal vibration detected. "
            "Possible crack formation, "
            "loose joints, or resonance."
        )

        solution = (
            "Inspect the structure, "
            "check beam-column joints, "
            "tighten supports, and "
            "perform maintenance."
        )

    else:

        problem = (
            "Structure operating normally."
        )

        solution = (
            "Continue monitoring regularly."
        )

    history = SensorData.objects.all().order_by(
        '-created_at'
    )[:10]

    context = {

        "frequency": frequency,

        "rms": rms,

        "result": status,

        "history": history,

        "severity": severity,

        "risk": risk,

        "problem": problem,

        "solution": solution,

        "ax": ax,

        "ay": ay,

        "az": az
    }

    return render(

        request,

        'dashboard.html',

        context
    )


    # ======================================
    # SEVERITY LOGIC
    # ======================================

    if rms < 0.5:

        severity = "LOW"

        risk = "SAFE"

    elif rms < 1.5:

        severity = "MEDIUM"

        risk = "WARNING"

    elif rms < 3:

        severity = "HIGH"

        risk = "DANGER"

    else:

        severity = "CRITICAL"

        risk = "CRITICAL"


    # ======================================
    # DATABASE HISTORY
    # ======================================

    history = SensorData.objects.all().order_by(
        '-created_at'
    )[:10]


    context = {

        "frequency": frequency,

        "rms": rms,

        "result": status,

        "history": history,

        "confidence": confidence,

        "severity": severity,

        "risk": risk
    }

    return render(

        request,

        'dashboard.html',

        context
    )


# ======================================
# AI PREDICTION PAGE
# ======================================

def predict_page(request):

    result = None

    damage_probability = None

    severity = None

    risk = None


    if request.method == "POST":

        frequency = float(
            request.POST.get("frequency")
        )

        rms = float(
            request.POST.get("rms")
        )


        # ======================================
        # AI PREDICTION
        # ======================================

        prediction = model.predict(
            [[frequency, rms]]
        )


        # ======================================
        # AI CONFIDENCE
        # ======================================

        probability = model.predict_proba(
            [[frequency, rms]]
        )

        damage_probability = round(
            probability[0][1] * 100,
            2
        )


        # ======================================
        # HEALTH RESULT
        # ======================================

        if prediction[0] == 0:

            result = "Healthy"

        else:

            result = "Damaged"


        # ======================================
        # SEVERITY LOGIC
        # ======================================

        if rms < 0.5:

            severity = "LOW"

            risk = "SAFE"

        elif rms < 1.5:

            severity = "MEDIUM"

            risk = "WARNING"

        elif rms < 3:

            severity = "HIGH"

            risk = "DANGER"

        else:

            severity = "CRITICAL"

            risk = "CRITICAL"


        # ======================================
        # SAVE SQLITE DATABASE
        # ======================================

        SensorData.objects.create(

            frequency=frequency,

            rms=rms,

            status=result
        )


        # ======================================
        # SAVE FIREBASE
        # ======================================

        ref = db.reference('sensor_data')

        ref.push({

            'frequency': frequency,

            'rms': rms,

            'status': result,

            'damage_probability':
            damage_probability
        })

        print(
            "Firebase Data Sent Successfully"
        )


        # ======================================
        # GENERATE PDF REPORT
        # ======================================

        generate_report(

            frequency,

            rms,

            result
        )


    return render(

        request,

        "predict.html",

        {

            "result": result,

            "damage_probability":
            damage_probability,

            "severity": severity,

            "risk": risk
        }
    )


# ======================================
# CHART DATA API
# ======================================

def get_chart_data(request):

    ref = db.reference(
        'sensor_data'
    )

    data = ref.get()

    labels = []

    rms_values = []

    frequency_values = []

    status_values = []


    if data:

        for key, value in data.items():

            labels.append(
                key[-5:]
            )

            rms_values.append(
                value.get('rms', 0)
            )

            frequency_values.append(
                value.get(
                    'frequency',
                    0
                )
            )

            status_values.append(
                value.get(
                    'status',
                    'Unknown'
                )
            )


    return JsonResponse({

        'labels': labels[-10:],

        'rms': rms_values[-10:],

        'frequency':
        frequency_values[-10:],

        'status':
        status_values[-10:]
    })