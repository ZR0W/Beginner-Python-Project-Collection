# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:18:04 2019

@author: Rowland 
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

print(np.pi)

print(math.pi)

t = np.arange(0.0, np.pi, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel="x axis", ylabel="y axis", title="Here's a sin function")
ax.grid()

fig.savefig("test.png")
plt.show()
