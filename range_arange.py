# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:03:22 2017

@author: tangwenhua
"""

import numpy as np
"""
range(start, end, step)，返回一个list对象，起始值为start，终止值为end，但不含终止值，步长为step。只能创建int型list。
arange(start, end, step)，与range()类似，但是返回一个array对象。需要引入import numpy as np，并且arange可以使用float型数据。
"""

a =[ i for i in range(1,10,2)]
print(a) #[1, 3, 5, 7, 9] range返回的是list对象



c = 18
s = np.arange(c)
print(s) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17]
