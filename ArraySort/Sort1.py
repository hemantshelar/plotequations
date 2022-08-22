import numpy as np
import matplotlib.pyplot as plt

import torch

bellCurveX = torch.randn(100)*10
bellCurveY = bellCurveX + torch.randn(100)*3
plt.plot(bellCurveX.numpy(),bellCurveY.numpy(),'*')
plt.ylabel('y')
plt.xlabel('x')
plt.show()