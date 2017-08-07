# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:11:21 2017

@author: lifan
"""
import math

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list

# or better yet...
"""
def get_primes(input_list):
    return (element for element in input_list if is_prime(element))
"""

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
    
print(get_primes([23,5345,23,4,23,423,54,564,3])) #[23, 23, 23, 3]
