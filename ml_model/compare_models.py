import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("vibration_data.csv")

# Features and labels
X = data[["Frequency", "RMS"]]

y = data["Damage"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
models = {
    "Random Forest": RandomForestClassifier(),

    "KNN": KNeighborsClassifier(),

    "MLP": MLPClassifier(max_iter=1000)
}

# Accuracy storage
accuracies = {}

# Train and test
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    accuracies[name] = accuracy

    print(f"{name} Accuracy: {accuracy}")

# Plot comparison graph
plt.bar(
    accuracies.keys(),
    accuracies.values()
)

plt.title("ML Model Comparison")

plt.xlabel("Models")

plt.ylabel("Accuracy")

plt.ylim(0, 1)

plt.show()