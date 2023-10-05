import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#p_coeff = [1, 0, 2j*np.sqrt(3), 0, 1]   # Numerator
#q_coeff = [1, 0, -2j*np.sqrt(3), 0, 1]   # Denominator

#p_coeff = [1 ,0, 0, 0, -11.19j, 0, 0, 0, -3.38, 0]
#q_coeff = [0 ,-3.38, 0, 0, 0, -11.19j, 0, 0, 0, 1]

#p_coeff = [0, np.sqrt(3)*1j, 0, -1]
#q_coeff = [1, 0, -np.sqrt(3)*1j, 0]

p_coeff = [ 0.333+0.085j, 0.783+0.721j, 5.716-0.909j, 0.518+6.499j, 5.853+0.399j, -2.893-4.355j, 3.337+4.251j, 1.726+1.312j, 0.132-1.538j, 0.544-0.231j ]
q_coeff = [ -0.387-0.553j, 0.593+0.573j, 2.764+1.891j, -0.758-1.546j, -2.035+0.092j, -12.025+2.715j, -1.816-4.195j, -3.371+0.582j, 1.893-0.792j, -0.151-0.287j ]


def polynomial_eval(coefficients, z):
    return np.polyval(coefficients, z)

def compute_density(z, p, p_prime, q, q_prime): #fix this density
    den1 = np.abs(p_prime * q - q_prime * p)
    den2 = np.real(q)**2 + np.imag(q)**2 + np.real(p)**2 + np.imag(p)**2
    return ((1 + np.real(z)**2 + np.imag(z)**2) * (den1/den2))**4

def integrand(x, y):
    z = x + 1j * y

    p = polynomial_eval(p_coeff, z)       # Initialize p
    q = polynomial_eval(q_coeff, z)       # Initialize q

    p_prime = polynomial_eval(np.polyder(p_coeff), z)
    q_prime = polynomial_eval(np.polyder(q_coeff), z)

    density = compute_density(z, p, p_prime, q, q_prime)

    return density

# Make data.
grid = 5
X = np.arange(-grid, grid, 0.01)
Y = np.arange(-grid, grid, 0.01)
X, Y = np.meshgrid(X, Y)
Z = integrand(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z,rstride=2,cstride=2, cmap=cm.jet,
                       linewidth=0, alpha=1, antialiased=True)

# Customize the z axis.
ax.set_zlim(0, 500)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=.5, aspect=5)

# Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([-grid, grid])
ax.set_yticks([-grid, grid])
ax.set_zticks([])

plt.show()
