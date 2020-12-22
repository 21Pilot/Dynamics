# Dynamics 
# Rod and free Collar problem 
# Answer code 
# Flora Seo 

# Set up 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define system constants
1 = 1 
mcollar = 1
mrod = 1
tau = 1
X0 = 0
V0 = 0
Q0 = 0
Z0 = 0


# Define Equation of Motion
def function(y, t, constants):
    
    X, V, Z, Q = Y
    mc, mr, tau, 1 = constants 
    denom = (1/3)*(mr)*(1**2) + (mc * X**2)
    dydt = [V, X*(Z**2), Z, ((Z*(-2)*(mc)*X*V))/(denom + tau/denom)] 
    return dydt

# initial set up 
y0 = [X0, V0, Z0, Q0]
# Create the samples for the output of the ODE solver
t = np.linspace(0, 1, 10001)
sol = odeint (function, y0, t, args=(parameters))


# Plot1 results
plt.title( 'collar displavement in sec')
plt.plot(t, sol[:, 0], 'g', label = 'x(t)')
plt.legend (loc='best')
plt.xlable('time (s)') 
plt.ylable('displacement (m)')
plt.grid ()
plt.show()

#Plot2 results
plt.title( 'Theta')
plt.plot(t, sol[:, 2], 'b', label = 'Theta(t)')
plt.legend (loc='best')
plt.xlable('time (s)') 
plt.ylable('Theta(rad)')
plt.grid ()
plt.show()

