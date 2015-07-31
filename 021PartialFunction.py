#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

'''
functools.partial帮助我们创建一个偏函数
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''

import functools
int2 = functools.partial(int, base=2)  # 相当于设置int函数的base参数的新的缺省值
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000', base=10))  # 此处将base参数仍旧设置成10

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)  # 实际上会把10作为*args的一部分自动加到左边
ret = max2(5, 6, 7)  # 相当于max(10, 5, 6, 7)
print(ret)
