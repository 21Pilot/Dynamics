# Flora Se
# Dynamics
# Oscillation 2.c

from scipy.integrate import odeint
import numpy as np
import matplolib.pyplot as plt

def spring(y,t,f,g):
  x,v = y 
  dydt = [v, -f*v-g*np.sin(x)]
  return dydt
  
# initial condition
b = 0.1
k = 900
m = 0.05

f = b//m
g = k/m

y0 = [0.01,0]
t= np.linspace(0,0.5,301)
# use odeint package to generate solution
sol = odeint(spring, y0, t, args = (f,g))

plt.plot(t,sol[:,0], 'b', label = 'x(t)')
plt.plot(t,sol[:,1}, 'g', label = 'v(t)')
plt.legend(loc = 'best')
plt.xlabel('t')
plt.sho()
