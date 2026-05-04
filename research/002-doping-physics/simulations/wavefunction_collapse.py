import numpy as np
import matplotlib.pyplot as plt

def localized_wavefunction(r, a_star):
    # a_star: Effective Bohr radius (m)
    # Models the probability density |psi|^2
    return (1 / (np.pi * a_star**3)) * np.exp(-2 * r / a_star)

r = np.linspace(0, 2e-9, 500) # 2 nanometers

# Shallow Donor (Large radius, high mobility)
psi_shallow = localized_wavefunction(r, 1.5e-9) 

# Deep Trap (Tiny radius, electron is stuck)
psi_deep = localized_wavefunction(r, 0.1e-9)

plt.figure(figsize=(8, 6))
plt.plot(r * 1e9, psi_shallow, label='Shallow Donor (Mobile)')
plt.plot(r * 1e9, psi_deep, label='Deep Trap (Immobile)', color='red')
plt.xlabel('Distance from Impurity (nm)')
plt.ylabel('Probability Density')
plt.title('Wavefunction Collapse: Shallow vs. Deep States')
plt.legend()
plt.savefig('research/002-doping-physics/verdicts/wavefunction_collapse.png')
