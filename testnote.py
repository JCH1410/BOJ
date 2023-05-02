import torch

a = torch.zeros(4, 2)
b = a.view(2, 4)
a.fill_(1)

print(b)