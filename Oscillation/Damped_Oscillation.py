# Flora Seo
# Dynamics
# Damped Oscillation 

import matplotlib.pyplot as plt
import numpy as np 
import math as mt

m =0.05
b = 0.1
k = 900
a = -1*b/(2*m)
b = np.sprt(4*m*k-b*b)/(2*m)
c1 = 0.01
c2 =0

e = mt.exp(1)
t = np.linspace(0,0.5,500)
y = (e**(a*t)*(c1*np.cos(b*t))

plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.title('Damped Oscillation Position Graph')
plt.show()

v = (a*e**(a*t))*(c1*np.cos(b*t))-(e**(a*t))*c1*-1*b*np.in(b*t)
plt.plot(t,v)
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.title('Damped Oscillation Velocity Graph')
plt.show()
