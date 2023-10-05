import numpy as np
import random

# -- Code to change coefficents of a Rational Map by a Mobius transform in the target space.

# Rational Map
p_coeff = [-0.517+0.070j, 1.190+1.875j, -1.129+2.014j, -1.135-2.330j, 6.428+4.729j, 4.232-2.729j, -2.623+6.480j, -0.053+2.471j, 0.757+2.280j, -0.345+0.013j]     # Numerator
q_coeff = [0.077-0.497j, 1.610+0.772j, 1.402-2.890j, -3.897+6.441j, 0.643+1.647j, 0.470+9.243j, -0.706+2.835j, -0.900-2.553j, 1.505+0.513j, 0.573-0.284j]    # Denominator

# Choose random a,b such that |a|^2 + |b|^2 = 1
def generate_complex_numbers():
    # Generate a random angle in radians
    angle_a = random.uniform(0, 2 * np.pi)

    # Calculate the magnitude of a using the relationship |a|^2 + |b|^2 = 1
    magnitude_a = np.sqrt(1 - random.random())

    # Calculate the magnitude of b
    magnitude_b = np.sqrt(1 - magnitude_a**2)

    # Convert polar coordinates to rectangular coordinates
    real_a = magnitude_a * np.cos(angle_a)
    imag_a = magnitude_a * np.sin(angle_a)

    # The imaginary part of b will be chosen randomly
    real_b = random.uniform(-magnitude_b, magnitude_b)
    imag_b = np.sqrt(magnitude_b**2 - real_b**2)

    # Account for negative imaginary part of b with a 50% chance
    if random.random() < 0.5:
        imag_b *= -1

    complex_a = complex(real_a, imag_a)
    complex_b = complex(real_b, imag_b)

    return complex_a, complex_b

#a, b = generate_complex_numbers()
a=(0.261-0.413j)
b=(-0.794-0.362j)

parameter_matrix = [[a, b], [-np.conjugate(b), np.conjugate(a)]]

def mob_trans_target (p_coeff, q_coeff, a, b):
    target_matrix = np.matmul(parameter_matrix, [p_coeff, q_coeff])

    global p_target_coeff
    global q_target_coeff

    p_target_coeff = target_matrix[0]
    q_target_coeff = target_matrix[1]

mob_trans_target (p_coeff, q_coeff, a, b)

# Format complex numbers in a+bj format without commas
def format_complex_number(num):
    if num.imag == 0:
        return f"{num.real:.3f}"
    elif num.real == 0:
        return f"{num.imag:.3f}j"
    else:
        return f"{num.real:.3f}{'+' if num.imag >= 0 else '-'}{abs(num.imag):.3f}j"

def format_complex_array(arr):
    formatted_arr = [format_complex_number(num) for num in arr]
    return ', '.join(formatted_arr)  # Join the formatted complex values

formatted_p_target_coeff = format_complex_array(p_target_coeff)
formatted_q_target_coeff = format_complex_array(q_target_coeff)

print(a)
print(b)
2
print("a = [",formatted_p_target_coeff,"]")
print("b = [",formatted_q_target_coeff,"]")
