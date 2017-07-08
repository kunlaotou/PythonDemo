def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  #[1, 4, 9, 16, 25, 36, 49, 64, 81]

               

 """              
用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，
得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
"""

from functools import reduce
def fn(x, y):
   return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))
