# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:57:12 2017

@author: tangwenhua
"""
import numpy as np
import pandas as pd

nb_classes = 4
targets = np.array([2, 3, 3, 3, 1, 3, 2, 3])

print(np.eye(nb_classes))
"""
[[ 1.  0.  0.  0.]
 [ 0.  1.  0.  0.]
 [ 0.  0.  1.  0.]
 [ 0.  0.  0.  1.]]
"""
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
"""
[[ 0.  0.  1.  0.]
 [ 0.  0.  0.  1.]
 [ 0.  0.  0.  1.]
 [ 0.  0.  0.  1.]
 [ 0.  1.  0.  0.]
 [ 0.  0.  0.  1.]
 [ 0.  0.  1.  0.]
 [ 0.  0.  0.  1.]]
"""
