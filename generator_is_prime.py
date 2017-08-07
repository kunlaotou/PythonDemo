# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:11:21 2017

@author: tangwenhua
1.generators are used to generate a series of values

2.yield is like the return of generator functions

3.The only other thing yield does is save the "state" of a generator function

4.A generator is just a special type of iterator

5.Like iterators, we can get the next value from a generator using next()
    for gets values by calling next() implicitly
"""
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
"""
Imagine what we could do if get_primes could simply return the next value 
instead of all the values at once. 
It wouldn't need to create a list at all. No list, no memory issues. 
"""

def get_primes(number):
    while True:
        if is_prime(number):
            yield number #当程序运行到yield时候，yield把值传给调用next()的人，同时保存generator function的状态
        number += 1
        
#求小玉10的素数之和
def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    #由于生成器是一种迭代器，因此可以在for循环中使用。
    for next_prime in get_primes(3):
        if next_prime < 1000:
            total += next_prime
        else:
            print(total)
            return
    
print(solve_number_10())    """
                            76127
                            None
