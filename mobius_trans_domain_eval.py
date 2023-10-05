import numpy as np
from sympy import *
import random

z = symbols('z', complex=True)

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
a=-0.252+0.836j
b=0.267-0.408j

p_coeff = [1 ,0, 0, 0, -11.19j, 0, 0, 0, -3.38, 0]
q_coeff = [0 ,-3.38, 0, 0, 0, -11.19j, 0, 0, 0, 1]

n = len(p_coeff) - 1  # n dimension

p = 0
q = 0

p = sum(p_coeff[i] * (-conjugate(b) * z + conjugate(a))**(n - i) * (a * z + b)**i for i in range(n + 1))
q = sum(q_coeff[i] * (-conjugate(b) * z + conjugate(a))**(n - i) * (a * z + b)**i for i in range(n + 1))

expanded_p = expand(p)
expanded_q = expand(q)

p_domain_trans = [0] * (n+1)
q_domain_trans = [0] * (n+1)

for i in range(0, n+1):
    p_domain_trans[i] = expanded_p.coeff(z, n-i)
    q_domain_trans[i] = expanded_q.coeff(z, n-i)

# Convert to NumPy complex arrays
p_domain_trans = np.array(p_domain_trans, dtype=np.complex128)
q_domain_trans= np.array(q_domain_trans, dtype=np.complex128)

# Format complex numbers in a+bj format without commas
def format_complex_number(num):
    if num.imag == 0:
        return f"{num.real:.3f}"
    elif num.real == 0:
        return f"{num.imag:.3f}j"
    else:
        return f"{num.real:.3f}{'+' if num.imag >= 0 else '-'}{abs(num  .imag):.3f}j"

def format_complex_array(arr):
    formatted_arr = [format_complex_number(num) for num in arr]
    return ', '.join(formatted_arr)  # Join the formatted complex values

formatted_p_domain_coeff = format_complex_array(p_domain_trans)
formatted_q_domain_coeff = format_complex_array(q_domain_trans)

print(a)
print(b)

print(formatted_p_domain_coeff)
print(formatted_q_domain_coeff)
