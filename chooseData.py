

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
print(df.ix[0,2])
###########################################################




L =[i for i in range(10)]   #[0,1,2,3,4,5,6,7,8,9] 
    
L1 = L[::2] #拿出偶数项的值    [0,2,4,6,8]
L2 = L[::-1] #倒序            [9,8,7,6,5,4,3,2,1,0]

print(L1)
print(L2)



a = [i for i in range(3)] #[0,1,2]

a[1:3] = [4, 5, 6]        #按index改变列表的值和长度
print(a)     #[0,4,5,6]
