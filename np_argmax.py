# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 14:39:03 2017

@author: tangwenhua
"""

import numpy as np

"""
1.首先min/max与np.argmin/np.argmax函数的功能不同
  前者返回值，后者返回最值所在的索引（下标）

2.处理的对象不同 
  前者跟适合处理list等可迭代对象，而后者自然是numpy里的核心数据结构ndarray（多维数组）

3.min/max是Python内置的函数
  np.argmin/np.argmax是numpy库中的成员函数
"""

a = np.arange(6)  #[0,1,2,3,4,5]
b = np.argmax(a)  
print(b)          #5







a1 = np.arange(6).reshape(2,3)  #[[0 1 2]
                                 #[3 4 5]]
b1 = np.argmax(a1) 
print(b1)        #5

c1 = np.argmax(a1, axis=0) #按照列来求最大值的索引
print(c1)       #[1 1 1]

c2 = np.argmax(a1, axis=1) #按照行来求最大值的索引
print(c2)      #[2 2]
