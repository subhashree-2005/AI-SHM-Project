import pandas as pd
import random

data = []

# Healthy structure data
for i in range(100):

    frequency = random.uniform(19, 21)
    rms = random.uniform(0.1, 0.3)

    data.append([frequency, rms, 0])

# Damaged structure data
for i in range(100):

    frequency = random.uniform(14, 18)
    rms = random.uniform(0.4, 0.8)

    data.append([frequency, rms, 1])

# Create dataframe
df = pd.DataFrame(data, columns=[
    "Frequency",
    "RMS",
    "Damage"
])

# Save CSV
df.to_csv("vibration_data.csv", index=False)

print("Dataset generated successfully!")