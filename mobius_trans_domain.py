import numpy as np
from sympy import *

n = 3 # dimension n

a, b, z = symbols('a, b, z', complex=True)

p_coeff = Matrix([symbols(f'p{n-i}') for i in range(0, n+1)])
p = 0

p = sum(p_coeff[i] * (-np.conjugate(b) * z + np.conjugate(a))**(n - i) * (a * z + b)**i for i in range(n + 1))

expanded_p = expand(p)
p_coeff_trans = zeros(1, n+1)

for i in range(0, n+1):
    p_coeff_trans[i] = expanded_p.coeff(z, n-i)
    print(p_coeff_trans[i])
