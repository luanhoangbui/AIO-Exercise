import torch
import torch . nn as nn


class MySoftmax (nn . Module):
    def __init__(self):
        super() . __init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdims=True)
        return x_exp/total


data = torch . Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
