#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

from collections import Iterable
print('迭代：利用for可以对一切可迭代的对象进行迭代')
print('*'*20)

print('通过collections模块的Iterable类型判断一个对象是否可以迭代')
print('isinstance(\'abc\', Iterable)')
print(isinstance('abc', Iterable))

print('isinstance([1, 2, 3], Iterable)')
print(isinstance([1, 2, 3], Iterable))

print('isinstance(123, Iterable)')
print(isinstance(123, Iterable))

print('\n', '*'*20)
print('迭代dictionary')
d = {'a': 1, 'b': 2, 'c':3}
print(d)
print('迭代key')
for key in d:
    print(key)
print('迭代value')
for value in d.values():
    print(value)
print('迭代key和value')
for k, v in d.items():
    print(k, v)

print('\n', '*'*20)
print('利用enumerate函数可以在for循环中同时迭代索引和元素本身')
list0to10 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
for i, value in enumerate(list0to10):
    print(i, value)
