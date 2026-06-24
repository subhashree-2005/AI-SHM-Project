# AI Structural Health Monitoring System

A Django-based Structural Health Monitoring (SHM) system that uses vibration data, machine learning, Firebase cloud database, and real-time dashboards to detect structural damage.

---

# Features

* Real-Time Structural Health Monitoring
* Machine Learning Based Damage Detection
* Firebase Cloud Database Integration
* Live Dashboard with Graphs
* FFT-Based Vibration Analysis
* Sensor Data Simulation
* PDF Report Generation
* Django Web Application

---

# Technologies Used

* Python
* Django
* Scikit-Learn
* Firebase Realtime Database
* HTML
* CSS
* JavaScript
* Chart.js
* NumPy
* Pandas
* Arduino
* MPU6050 Sensor

---

# Project Structure

AI_SHM_Project/

├── app/

├── ml_model/

├── project3/

├── templates/

├── manage.py

├── simulate_sensor.py

├── dataset_analysis.py

├── requirements.txt

└── README.md

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Django Server

```bash
python manage.py runserver
```

---

# Demo Workflow

Open a second terminal and activate the virtual environment:

```bash
venv\Scripts\activate
```

Run the live sensor simulator:

```bash
python simulate_sensor.py
```

This continuously sends vibration data to Firebase and updates the dashboard in real time.

---

# Presentation Checklist

Start Django Server:

```bash
python manage.py runserver
```

Start Live Sensor Simulation:

```bash
python simulate_sensor.py
```

Open Home Page:

```text
http://127.0.0.1:8000/
```

Open Dashboard:

```text
http://127.0.0.1:8000/dashboard/
```

Open AI Prediction Page:

```text
http://127.0.0.1:8000/predict-page/
```

Run Dataset Analysis:

```bash
python dataset_analysis.py
```

Run Machine Learning Comparison:

```bash
python ml_model/compare_models.py
```

Check Firebase Data:

Open Firebase Console and verify live sensor values are updating.

---

# Machine Learning Features

* Frequency-based Damage Detection
* RMS Vibration Analysis
* Healthy vs Damaged Classification
* Real-Time Structural Monitoring
* Confidence-Based Predictions

---

# Author

Subhashree Aich

B.Tech Artificial Intelligence & Machine Learning

Structural Health Monitoring Research Project
