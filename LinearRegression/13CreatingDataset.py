import torch
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


x = torch.randn(100,1)
bellCurve = x.numpy()
print(bellCurve)
bellCurve = np.sort(bellCurve,axis=None)
print(bellCurve)
#plt.plot(xNumPy,norm.pdf(xNumPy,0,1))

#bellCurve = np.linspace(-2,2,100) 

plt.plot(bellCurve,norm.pdf(bellCurve,1,2))



#plt.plot(x.numpy(),y.numpy(),".")
plt.show()
