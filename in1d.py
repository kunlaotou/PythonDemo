import numpy as np
import pandas as pd

test = np.array([0, 1, 2, 5, 0])
states = [0, 2]
mask = np.in1d(test, states)  #相当于test[mask]
print(mask) #[ True False  True False  True]
print(test[mask]) #[0 2 0]

mask = np.in1d(test, states, invert=True)
print(mask) #[False  True False  True False]
print(test[mask]) #[1 5]
