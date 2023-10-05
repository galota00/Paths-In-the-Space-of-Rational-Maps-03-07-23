import numpy as np
import matplotlib.pyplot as plt

# ---------- Computes I along a path in the space of rational maps ----------

# Map 1
#a = [1 ,0, 0, 0, -11.19j, 0, 0, 0, -3.38, 0]   # Numerator
#b = [0 ,-3.38, 0, 0, 0, -11.19j, 0, 0, 0, 1]   # Denominator
# Map 2
#a = [ 0.759-0.594j, 0.184-0.125j, -2.008-0.279j, 1.350+1.533j, -2.716-5.584j, 0.283-0.429j, -4.258+8.140j, -0.538+0.632j, -2.578+0.538j, -0.247-0.015j ]
#b = [ -0.314+0.038j, 1.521+0.389j, -5.251-3.914j, -1.723-2.743j, -0.298-4.633j, -1.900+3.423j, 3.197-2.211j, 2.692-0.669j, -0.091+0.092j, -0.740-0.580j ]

#c = [0 ,-1.98, 0, 12.09j, 0, -7.02, 0, 1.77j, 0, 1]   # Numerator
#d = [-1 ,0, -1.77j, 0, 7.02, 0, -12.09j, 0, 1.98, 0]   # Denominator

a = [1, 0, 3.94j, 0, -3.07, 0]
b = [0, -3.07, 0, 3.94j, 0 ,1]
# Map 2
c = [1, 0, 0, 0, -5, 0]
d = [0, -5, 0, 0, 0 ,1]

# Create functions f(t) and g(t) that map between coefficients
def interpolate_coeffs(a, c, t):
    if len(a) != len(c):
        raise ValueError("Lists 'a' and 'c' must have the same length for interpolation.")
    return [a[i] + t * (c[i] - a[i]) for i in range(len(a))]

def polynomial_eval(coefficients, z):
    return np.polyval(coefficients, z)

def compute_density(z, p, p_prime, q, q_prime): #fix this density
    den1 = np.abs(p_prime * q - q_prime * p)
    den2 = np.real(q)**2 + np.imag(q)**2 + np.real(p)**2 + np.imag(p)**2
    return ((1 + np.real(z)**2 + np.imag(z)**2)**2) * (den1/den2)**4


def integrand(x, y, t):
    f = interpolate_coeffs(a, c, t)
    g = interpolate_coeffs(b, d, t)
    z = x + 1j * y

    p = polynomial_eval(f, z)       # Initialize p
    q = polynomial_eval(g, z)       # Initialize q

    p_prime = polynomial_eval(np.polyder(f), z)
    q_prime = polynomial_eval(np.polyder(g), z)

    density = compute_density(z, p, p_prime, q, q_prime)

    return density
# ------------------------------------------------------------------------------

size = 10           # [-size,size] x [-size,size] grid
step = 0.1            # step size
comp = 100         # no. of computations along path is comp+1

til = int(size/step)      # no. of tiles is 2*til^2

t_points = np.zeros(comp + 1)
I_points = np.zeros(comp + 1)

for k in range(comp + 1):
    time = k/comp
    t_points[k] = time
    integral = 0
    for i in range(-til, til):
        for j in range(-til, til):
            integral = integral + integrand(i*step, j*step, time)*(step**2)
    integral = integral / np.pi
    I_points[k] = integral

    #print(time ,integral)
    print(integral)

plt.plot(t_points, I_points, color='red')
plt.show()
