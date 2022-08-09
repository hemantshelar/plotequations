import torch
import numpy as np
import matplotlib.pyplot as plt

v = torch.tensor([1,2,3,4,5,6])

print(v)

print('slicing..')
print(v[:3])

lst = list(("a","B"))
lst.append(1)

print (lst)

ft = torch.FloatTensor([1,2,3,4,5,6,7])
print(ft)

#x = ft.view(6,1)
#print(x)

x = ft.view(1,-1)
print(x)

a = np.array([1,2,3,4,5,6])
fromNumpy = torch.from_numpy(a)
print(fromNumpy)

v1 = torch.tensor([1,2,3])
v2 = torch.tensor([1,2,3])

v3 = v1 + v2
print(v3)

mul = v1 * 5
print ( mul)

dot_prod = torch.dot(v1,v2)
print(dot_prod)

x = torch.linspace(0,10,1000)
y = torch.exp(x)
#y = torch.sin(x)
#y = torch.cos(x)
#y = torch.tan(x)

plt.plot(x.numpy(),y.numpy())
plt.show()