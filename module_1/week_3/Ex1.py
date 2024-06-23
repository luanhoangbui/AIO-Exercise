import torch
import torch.nn as nn

data = torch.Tensor([1, 2, 3])

tensor([1., 2., 3.])

softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)

tensor([0.0900, 0.2477, 0.6652])


class Softmax(nn.Module):
    def __init__(self):
        supper().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdims=True)
        return x_exp/total


softmax_1 = Softmax()
output = softmax_1(data)

tensor([0.0900, 2.447, 0.6652])


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdims=True)
        return x_exp/total


stable_softmax_1 = StableSoftmax()
output = stable_softmax_1(data)

tensor([0.0900, 0.2447, 0.6652])

tensor([1., 2., 3.])
