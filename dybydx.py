import torch;

#  f (x) = 9x^4 + 2x^3 + 3x^2 + 6x + 1
#  f'(x) = 36x^3 + 6x^2 + 6x + 0
#  f'(2) = 36 * 2^2 + 6*2^1 + 6
#  f'(2) = 330


def f(x):
  return 36*x**3 + 6*x**2 + 6
x = torch.tensor(2.0,requires_grad=True)

y = 9*x**4 + 2*x**3 + 3*x**2 + 6*x + 1
y.backward()

print(x.grad)


x = torch.tensor(1.0,requires_grad=True)
z = torch.tensor(2.0,requires_grad=True)

y = x**2 + z**3
y.backward()

print(x.grad)
print(z.grad)

