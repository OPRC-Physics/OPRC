import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    Ei = np.linspace(0.01, 0.6, 100) # Ionization Energy in eV
    T = 300 # Temperature in Kelvin
    kb = 8.617e-5 # Boltzmann constant
    
    # Efficiency calculation based on Fermi-Dirac statistics
    eta = 1 / (1 + 2 * np.exp(Ei / (kb * T)))
    
    plt.figure(figsize=(8, 6))
    plt.plot(Ei, eta, linewidth=2)
    plt.xlabel('Ionization Energy (eV)')
    plt.ylabel('Dopant Efficiency')
    plt.title('OPRC Trap-Transition Curve')
    plt.grid(True)
    plt.savefig('research/002-doping-physics/verdicts/trap_curve.png')

if __name__ == "__main__":
    run_simulation()
