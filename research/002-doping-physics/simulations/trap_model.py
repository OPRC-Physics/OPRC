import numpy as np 
def calculate_ionization(Ei, T): 
    kb = 8.617e-5 
    return np.exp(-Ei / (kb * T)) 
print("Ionization Probability Calculated") 
