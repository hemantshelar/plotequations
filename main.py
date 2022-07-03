import numpy as np
import matplotlib.pyplot as plt
import math

def ymxc(m,x,c):
  return m*x + c; 

def circle(r,x):
  #
  #ySquare = r*r - x*x
  #ySquare = np.abs(ySquare)
  #y = np.sqrt(ySquare)
  y = np.sqrt(-x**2 + r**2)
  return y

r = 6

x = np.linspace(-r,r,1000)

#yline = ymxc(-1,x,-3)

ycircle = circle(2,x)


#plt.plot(x,yline)
plt.plot(x,ycircle)
plt.plot(x,-ycircle)

plt.grid()
plt.show()




