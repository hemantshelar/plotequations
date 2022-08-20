import torch

from torch.nn import Linear

torch.manual_seed(1)
model = Linear(in_features=1,out_features=1)

print(f'{model.bias} and {model.weight}')

x = torch.tensor([2.0])
result = model.forward(x)

print(result)

result = model(x)

print(result)