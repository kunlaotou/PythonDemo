# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:57:12 2017

@author: tangwenhua
"""

a = '''ALL that doth flow we cannot liquid name or else would fire and water
be the same;but that is liquid which is moist and wet Fire that property can
never get.Then 'tis not cold that doth the fire put out'.But 'tis te '''

print(a.startswith('ALL')) #True 这句话是否以’ALL‘开头
print(a.endswith('is')) #False 这句话是否以’is‘结尾

print(a.find('t')) #73 第一次出现t的位置
print(a.rfind('t')) #213 最后一次出现t的位置
print(a.count('t')) #26 这句话出现t的次数
print(a.isalnum()) #False 这段话所有的字符都输字母和数字吗？  
