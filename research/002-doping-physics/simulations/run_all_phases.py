import numpy as np
import matplotlib.pyplot as plt

# Create output folder recursively just in case
import os
os.makedirs('research/002-doping-physics/verdicts', exist_ok=True)

# ==========================================
# PHASE 1: Doping-Trap Efficiency Curve
# ==========================================
Ei = np.linspace(0.01, 0.6, 100)
T = 300 # Kelvin
kb = 8.617e-5
eta = 1 / (1 + 2 * np.exp(Ei / (kb * T)))

plt.figure(figsize=(6, 4))
plt.plot(Ei, eta, color='blue', linewidth=2)
plt.xlabel('Ionization Energy (eV)')
plt.ylabel('Dopant Efficiency')
plt.title('Phase 1: The OPRC Efficiency Cliff')
plt.grid(True)
plt.tight_layout()
plt.savefig('research/002-doping-physics/verdicts/phase1_efficiency.png')
plt.close()

# ==========================================
# PHASE 2: Wavefunction Confinement
# ==========================================
r = np.linspace(0, 2e-9, 500)
def psi_sq(distance, Bohr_radius):
    return (1 / (np.pi * Bohr_radius**3)) * np.exp(-2 * distance / Bohr_radius)

psi_shallow = psi_sq(r, 1.5e-9) # Spread out
psi_deep = psi_sq(r, 0.15e-9)   # Highly localized

plt.figure(figsize=(6, 4))
plt.plot(r * 1e9, psi_shallow, label='Shallow Donor (1.5 nm)', color='green')
plt.plot(r * 1e9, psi_deep, label='Deep Trap (0.15 nm)', color='red')
plt.xlabel('Radial Distance r (nm)')
plt.ylabel('Probability Density |ψ|²')
plt.title('Phase 2: Spatial Confinement')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('research/002-doping-physics/verdicts/phase2_confinement.png')
plt.close()

# ==========================================
# PHASE 3: Tunneling Probability
# ==========================================
# Calculates tunneling between two impurities as a function of separation distance d
d = np.linspace(0.5e-9, 5e-9, 100) # 0.5 to 5 nm
m_eff = 0.19 * 9.109e-31 # Effective mass in Silicon (longitudinal)
hbar = 1.054e-34

def tunneling_probability(dist, barrier_height_eV):
    V_0 = barrier_height_eV * 1.602e-19
    kappa = np.sqrt(2 * m_eff * V_0) / hbar
    return np.exp(-2 * kappa * dist)

T_shallow = tunneling_probability(d, 0.045) # Shallow barrier
T_deep = tunneling_probability(d, 0.54)    # Deep barrier

plt.figure(figsize=(6, 4))
plt.semilogy(d * 1e9, T_shallow, label='Shallow Tunneling (V₀ = 0.045 eV)', color='green')
plt.semilogy(d * 1e9, T_deep, label='Deep Tunneling (V₀ = 0.54 eV)', color='red')
plt.xlabel('Impurity Separation d (nm)')
plt.ylabel('Tunneling Probability (Log)')
plt.title('Phase 3: Quantum Tunneling Suppression')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.savefig('research/002-doping-physics/verdicts/phase3_tunneling.png')
plt.close()

print("All three OPRC Phases computed successfully!")
