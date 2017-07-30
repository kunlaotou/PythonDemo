# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:57:12 2017

@author: tangwenhua
"""
import numpy as np
import pandas as pd
import datetime as dt


data = np.arange(0,16).reshape(4,4)
data = pd.DataFrame(data,columns=['0','1','2','3'])
"""
[[ 0  1  2   3]
 [ 4  5  6   7]
 [ 8  9  10  11]
 [12  13 14 15]
]]
"""
def f(x):
    return x-2

#对列元素进行apply()函数
print(data.ix[:,['0','1']].apply(f))
"""
    0   1
0  -2  -1
1   2  -3
2   6   7
3  10  11
"""

#对行元素进行apply()函数
print(data.ix[[0,1],:].apply(f))
"""
   0  1  2  3
0 -2 -1  0  1
1  2  3  4  5
"""
#对行元素进行apply()函数
print(data.apply(f,axis = 1))
"""
    0   1   2   3
0  -2  -1   0   1
1   2   3   4   5
2   6   7   8   9
3  10  11  12  13
"""
