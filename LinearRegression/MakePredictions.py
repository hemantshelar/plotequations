import torch
import matplotlib.pyplot as plt
import numpy as np

def forward(x,w,b):
  y = w*x +b
  return y


w = torch.tensor(3.0,requires_grad=True) 
b = torch.tensor(1.0,requires_grad=True) 

x = torch.tensor([[2],[3]])
print(forward(x,w,b))