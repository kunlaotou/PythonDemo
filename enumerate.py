"""

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中。



参数
sequence -- 一个序列、迭代器或其他支持迭代对象。

返回值
返回 enumerate(枚举) 对象。

"""
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))  #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

print(list(enumerate(seasons, start=1))) # 小标从 1 开始 [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
