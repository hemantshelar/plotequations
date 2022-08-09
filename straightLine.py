import torch
import numpy as np
import matplotlib.pyplot as plt

def fun(m,x,c):
  return m*x + c

x = torch.linspace(1,100,1000)
x = np.linspace(-50,100,1000)

# y = 2x + 5

 
print(plt.style.available)

y = fun(2,x,5)
plt.style.use('fivethirtyeight')
#plt.axhline(0)
#plt.axvline(0)
plt.plot(x,y)
plt.grid()
plt.show()

