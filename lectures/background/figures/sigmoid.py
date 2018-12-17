#!/usr/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


y = np.linspace(-5, 5, 20)
z = sigmoid(y)

mpl.rc('font', size=14)

plt.close('all')
plt.figure()
plt.plot(y, z)
plt.xlabel('y')
plt.ylabel('z')
plt.title('Sigmoid function')
plt.annotate('Small derivative',
            xy=(4.5, 1), xytext=(2.5, 0.75),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Small derivative',
            xy=(-4.5, 0), xytext=(-5, 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show(block=False)
plt.savefig('sigmoid.pdf')
