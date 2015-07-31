#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""

list_0to9 = range(10)
print(list(list_0to9))

def power(x):
    return x * x

result = map(power, list_0to9)
print(list(result))

result = map(str, list_0to9)
print(list(result))

"""
 reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
"""
from functools import reduce

def add(x, y):
    return x + y

result = reduce(add, list_0to9)  # 前后两个元素相加，计算整个列表的总和
print(result)

def fn(x, y):
    return x * 10 + y
result = reduce(fn, list_0to9)  # 将列表变成一个整数
print(result)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

result = str2int("987654321")  # 字符串变整数
print(result)

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    int_part = s[0:s.find('.')]
    float_part = s[s.find('.')+1:]
    int_value = reduce(lambda x, y: x * 10 + y, map(char2num, int_part))
    float_value = reduce(lambda x, y: x * 10 + y, map(char2num, float_part))
    return float(int_value + float_value/(pow(10, (len(str(float_value))))))

print('str2float(\'123.456\') =', str2float('123.456'))