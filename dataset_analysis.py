import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
file = "Jayanth_data_nit.xlsx"
df = pd.read_excel(
    file,
    sheet_name="Graph (2)"
)

# Select columns
df = df[
    [
        "Frequency",
        "Acceleration per unit force per sec"
    ]
]

# Remove empty values
df = df.dropna()

# Rename columns
df.columns = ["Frequency", "Acceleration"]

# Create damage labels
# Example logic:
# High acceleration = damaged

df["Damage"] = (
    df["Acceleration"] > df["Acceleration"].mean()
).astype(int)

# Features
X = df[
    [
        "Frequency",
        "Acceleration"
    ]
]

# Target
y = df["Damage"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save model
joblib.dump(
    model,
    "advanced_damage_model.pkl"
)

print("Model Saved Successfully!")

# Plot graph
plt.plot(
    df["Frequency"],
    df["Acceleration"]
)

plt.xlabel("Frequency")
plt.ylabel("Acceleration")

plt.title("SHM Frequency Response")

plt.show()