#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-5, 5, 20)
y = sigmoid(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sigmoid function')
plt.show(block=False)
plt.savefig('sigmoid.pdf')
