import numpy as np 
def calculate_shift(r_cc, Z_eff, epsilon): 
    # r_cc: Radius of central cell (m) 
    # Z_eff: Effective charge difference 
    e_charge = 1.602e-19 
    eps_0 = 8.854e-12 
    delta_V = (Z_eff * e_charge) / (4 * np.pi * epsilon * eps_0 * r_cc) 
    return delta_V 
print("Central Cell Shift Calculation Ready") 
