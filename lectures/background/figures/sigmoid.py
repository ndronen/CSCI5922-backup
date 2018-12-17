#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-5, 5, 20)
y = sigmoid(x)

plt.close('all')
plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sigmoid function')
plt.annotate('Small derivative',
            xy=(4.5, 1), xytext=(2.5, 0.75),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Small derivative',
            xy=(-4.5, 0), xytext=(-5, 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show(block=False)
plt.savefig('sigmoid.pdf')
