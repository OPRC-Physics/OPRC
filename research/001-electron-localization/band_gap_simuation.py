import numpy as np
import matplotlib.pyplot as plt

def kronig_penney_rhs(alpha_a, P):
    """Calculates the Right Hand Side of the KP transcendental equation."""
    # To handle the limit where alpha_a approaches 0
    with np.errstate(divide='ignore', invalid='ignore'):
        rhs = P * np.sin(alpha_a) / alpha_a + np.cos(alpha_a)
    return rhs

# Physical Parameters for an 'Ideal Insulator'
P = 10.0  # High scattering power (Binding strength)
alpha_a = np.linspace(0.1, 20, 1000)
rhs_values = kronig_penney_rhs(alpha_a, P)

# Plotting the Energy States
plt.figure(figsize=(10, 6))
plt.plot(alpha_a, rhs_values, label=r'$P \frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a)$', color='blue')

# The "Conduction" boundaries: |RHS| must be <= 1 for an electron to be 'free'
plt.axhline(y=1, color='red', linestyle='--', alpha=0.5)
plt.axhline(y=-1, color='red', linestyle='--', alpha=0.5)

# Highlighting the Forbidden Gaps (Insulating behavior)
plt.fill_between(alpha_a, -5, 5, where=(np.abs(rhs_values) > 1), 
                 color='grey', alpha=0.3, label='Forbidden Energy Gap (No Free Electrons)')

plt.ylim(-2, 4)
plt.title(f"RFC #1: Energy Band Gap Formation (Scattering Power P={P})")
plt.xlabel(r'$\alpha a$ (Energy Proportionality)')
plt.ylabel('Probability Amplitudes')
plt.legend()
plt.grid(True, which='both', linestyle=':', alpha=0.5)

# Save for the technical note artifact
plt.savefig('insulator_gap_plot.png')
plt.show()
