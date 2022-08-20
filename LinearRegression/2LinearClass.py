import torch
from torch.nn import Linear
import matplotlib.pyplot as plt

# y = m*x + c
# y = weight*x + bias

def line(c,m,x):
  return m*x + c
def draw_line(b,w):
  x = torch.linspace(-14,14,100)
  y = line(b,w,x.numpy())

  plt.plot(x.numpy(),y)
  plt.grid()
  plt.show()

#torch.manual_seed(1)
model = Linear( in_features=1,out_features=1)
bias = model.bias.item()
weight = model.weight.item()

print( f'Bias(Y-intercept ) = {bias} and weight ( slop ) = {weight}')


#x = torch.tensor([2.0])
#print(model(x), model.forward(x))
draw_line(bias,weight)



