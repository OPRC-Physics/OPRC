import numpy as np
import matplotlib.pyplot as plt

def conduction_probability(Eg, T):
    kb = 8.617e-5  # Boltzmann constant in eV/K
    return np.exp(-Eg / (2 * kb * T))

# Parameters
Eg_insulator = 5.0  # 5 eV gap
temperatures = np.linspace(100, 2000, 500) # Kelvin

prob_insulator = conduction_probability(Eg_insulator, temperatures)

plt.figure(figsize=(10, 6))
plt.semilogy(temperatures, prob_insulator, label='Ideal Insulator (Eg=5eV)', color='green')
plt.axvline(x=300, color='blue', linestyle='--', label='Room Temp (300K)')

plt.title("RFC #1: Probability of Free Electron Excitation")
plt.xlabel("Temperature (K)")
plt.ylabel("Relative Carrier Concentration (log scale)")
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend()
plt.savefig('thermal_proof.png')
plt.show()
