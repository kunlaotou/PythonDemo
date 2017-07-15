# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:03:22 2017

@author: tangwenhua
"""

dict = {'a':32,'b':3,'c':356,'d':3452,'e':78972,'f':82,'g':3234,'h':2}

#提取字典里的键
print(dict.keys()) #dict_keys(['e', 'c', 'f', 'g', 'h', 'd', 'b', 'a'])

#提取字典里的值 传统的方法
if 'key' in dict:  
  print(dict['key'])   
else:   
  print('not found')   
 
"""
Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。

返回指定键的值，如果值不在字典中返回默认值None。
"""
a = dict.get("key","该键不在字典中")
print(a) # 该键不在字典中
