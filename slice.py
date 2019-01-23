# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:57:12 2017

@author: tangwenhua
"""


"""
[:]提取从开头到结尾的整个字符串
[star:]从start提取到结尾
[:end]从开头提取到end-1
[start:end]从start提取到end-1
[start:end:step]从start提取到end-1，每step个字符提取一个

注意：分片中end的偏移量要比实际提取的最后一个字符偏移量多1
"""

a = 'abcdefgtangwenhua'

print(a[:]) #abcdefgtangwenhua
print(a[4:]) #efgtangwenhua
print(a[:5]) #abcde
print(a[3:8]) #defgt
print(a[3:8:1]) #defgt
print(a[3:8:2]) #dft      从第三位提取到第八位，步长为2
print(a[::2]) #acegageha  从开头提取到结尾，步长为2
print(a[5::2]) #ftnwnu    从偏移量5，提取到结尾，步长设置为2
print(a[:14:2]) #acegage  从开头提取到偏移量13，步长为2
print(a[::-1]) #auhnewgnatgfedcba  反向输出
print(a[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
print(a[-3:]) #截取倒数第三位到结尾
print(a[:-5:-3]) #逆序截取，具体啥意思没搞明白？
