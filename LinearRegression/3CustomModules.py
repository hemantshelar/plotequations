import torch
import torch.nn as nn

# Crete Linear Regression class
# nn.Module is a base class for all NN modules.


class LR(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = nn.Linear(in_features=in_features,
                                out_features=out_features)
    def forward(self,x):
      result = self.linear(x) 
      return result

torch.manual_seed(1)
model = LR(1, 1)
print(list(model.parameters()))

x = torch.tensor([[1.0],[2.0]])
result = model.forward(x)
print(result)
