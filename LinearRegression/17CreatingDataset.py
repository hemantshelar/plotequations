import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

class LR(nn.Module):
  def __init__(self,input_size,output_size):
    super().__init__()
    self.linear = nn.Linear(input_size,output_size)
  def forward(self,x):
    result = self.linear.forward(x)
    return result

def plot_bell_curve(tensorX):
  pass

def plot_fit(title,w,b,x,y):
  plt.title = title
  x1 = np.array([-30,30])
  y1 = w*x1 + b
  plt.plot(x1,y1,'r')
  plt.scatter(x,y)

def get_params(model):
#print(list(model.parameters()))
  [w,b] = model.parameters()
  weight = w[0][0]
  bias = b[0]
  return(weight.item(),bias.item())

#Returns a tensor, filled with a random numbers that are norammly distributed.
#
x = torch.randn(100,1) * 10
y = x + torch.randn(100,1)*3


#plt.plot(bellCurve,norm.pdf(bellCurve,1,2))

torch.manual_seed(1)
model = LR(1,1)
(w,b) = get_params(model)
plot_fit('tite',w,b,x.numpy(),y.numpy())
print(w,b)



plt.show()


