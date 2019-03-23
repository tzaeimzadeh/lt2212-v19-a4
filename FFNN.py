import numpy as np
import math
import pandas
import torch

#https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
class neuralNetwork:
    def __init__(self, x, y, b, c, N, M):
        self.input = x
        self.b = 1
        self.c = 1
        self.N = N
        self.M = M
        self.weight1 = np.random.rand(self.input.shape[1], N)
        self.weight2 = np.random.rand(N, M)
        self.y = y
        self.output = np.zeros(y.shape)

    def crossEntropy(self, yHat):
        self.yHat = yHat # ?
        if y == 1: # self.y
            return -math.log(yHat)
        else:
            return -math.log(1-yHat)

    def feedForward(self):
        self.layer1 = torch.sigmoid(torch.mul(self.weight1, self.X) + self.b)
        self.layer2 = torch.softmax(torch.mul(self.weight2, self.layer1) + self.c)

    def train(self, X, y, epochs = 1): # L, M, N
        self.weight1 = torch.randn(L, M, requires_grad=True)
        self.b = torch.randn(M, requires_grad=True)
        self.weight2 = torch.randn(M, N, requires_grad=True)
        self.c = torch.randn(N, requires_grad=True)
        # adam optimizer
        # do i need to go element by element ?
        self.feedForward()
        # where do i get the y from? outside? 
        loss = crossEntropy(y, yhat) # this should be a torch object?
        loss.backward()



# net = neuralNetwork()