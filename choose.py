

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:41:25 2017

@author: Administrator

"""
import numpy as np
import pandas as pd






df = pd.DataFrame(np.arange(0,60,2).reshape(10,3),columns=list('abc'))

print(df)

#如果你知道column names 和index，且两者都很好输入，可以选择 .loc
#print(df.loc[0, 'b']) 
#print(df.loc[0:3, ['a', 'b']]  )  
#print(df.loc[[1, 5], ['b', 'c']] ) 

#如果嫌column name太长了，或者index是一列时间序列，更不好输入，那就可以选择 .iloc了。这边的 i 我觉得代表index，比较好记点。
print(df.iloc[1,1])
print(df.iloc[0:3, [0,1]]) 
print(df.iloc[[0, 3, 5], 0:2])

#ix 的功能就更强大了，它允许我们混合使用下标和名称进行选取。 可以说它涵盖了前面所有的用法。基本上把前面的都换成df.ix 都能成功
#但是有一点，就是df.ix [ [ ..1.. ], [..2..] ],  1框内必须统一，必须同时是下标或者名称，2框也一样。
