import numpy as np 
import matplotlib.pyplot as plt 
Ei = np.linspace(0.01, 0.6, 100) 
T = 300 
kb = 8.617e-5 
eta = 1 / (1 + 2 * np.exp(Ei / (kb * T))) 
plt.plot(Ei, eta) 
plt.xlabel('Ionization Energy (eV)') 
plt.ylabel('Dopant Efficiency') 
plt.title('OPRC Trap-Transition Curve') 
plt.savefig('research/002-doping-physics/verdicts/trap_curve.png') 
