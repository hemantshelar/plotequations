import matplotlib.pylab as plt
import numpy as np
import random as rnd

def getData():
  x = []
  y = []
  for i in range(10):
    x.append(i)
    y.append(rnd.randrange(10))
  return x,y

fig = plt.figure()

x , y = getData()
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(339)


ax1.plot(x,y)
x , y = getData()
ax2.plot(x,y)

x = np.linspace(0,100,1000)
y = np.sin(x)

ax3 = fig.add_subplot(337)
ax3.plot(x,y)

ax3 = fig.add_subplot(3,3,4)
y = np.cos(x)
ax3.plot(x,y,'*')
plt.show()