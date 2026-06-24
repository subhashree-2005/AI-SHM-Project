import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000

# Time axis
t = np.linspace(0, 1, fs)

# Healthy structure signal (20 Hz)
healthy_signal = np.sin(2 * np.pi * 20 * t)

# Damaged structure signal (16 Hz)
damaged_signal = np.sin(2 * np.pi * 16 * t)

# FFT for healthy structure
healthy_fft = np.fft.fft(healthy_signal)

# FFT for damaged structure
damaged_fft = np.fft.fft(damaged_signal)

# Frequency axis
frequencies = np.fft.fftfreq(len(t), 1/fs)

# Magnitudes
healthy_magnitude = np.abs(healthy_fft)
damaged_magnitude = np.abs(damaged_fft)

# Plot graph
plt.figure(figsize=(10,5))

plt.plot(
    frequencies[:500],
    healthy_magnitude[:500],
    label="Healthy Structure"
)

plt.plot(
    frequencies[:500],
    damaged_magnitude[:500],
    label="Damaged Structure"
)

plt.title("FFT Comparison: Healthy vs Damaged")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.legend()

plt.grid()

plt.show()