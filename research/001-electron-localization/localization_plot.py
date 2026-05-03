import numpy as np
import matplotlib.pyplot as plt

def localized_wannier(x, center, width):
    return np.exp(-(x - center)**2 / (2 * width**2))

def delocalized_bloch(x, k):
    return np.cos(k * x)

x = np.linspace(-10, 10, 1000)

# Insulator: High localization (small width)
insulator_state = localized_wannier(x, 0, 0.5)

# Metal: Delocalized wave (Bloch state)
metal_state = delocalized_bloch(x, 2)

plt.figure(figsize=(12, 6))

# Plot Insulator
plt.subplot(1, 2, 1)
plt.plot(x, insulator_state**2, color='red', lw=2)
plt.title("Insulator: Localized Electron Density\n(Wannier State)")
plt.xlabel("Position (x)")
plt.ylabel(r"$|\psi|^2$")
plt.fill_between(x, insulator_state**2, color='red', alpha=0.1)

# Plot Metal
plt.subplot(1, 2, 2)
plt.plot(x, metal_state**2, color='blue', lw=1)
plt.title("Metal: Delocalized Electron Density\n(Bloch State)")
plt.xlabel("Position (x)")
plt.ylabel(r"$|\psi|^2$")
plt.fill_between(x, metal_state**2, color='blue', alpha=0.1)

plt.tight_layout()
plt.savefig('localization_comparison.png')
plt.show()
