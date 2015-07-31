#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __author__ = 'zhang.c.m'

import math

def checking_input_for_quadratic(a, b, c):
    tuple_input = (a, b, c)
    for x in tuple_input:
        if not isinstance(x, (int, float)):
            print('请使用int型或float型')
            return False
    if a == 0:
        print('a不可以等于0')
        return False
    return True

def quadratic(a, b, c):
    if not checking_input_for_quadratic(a, b, c):
        return
    delta = b*b - 4 * a * c
    if delta < 0:
        print('本题无解')
    else:
        x1 = ((b*(-1)) + math.sqrt(delta))/(2*a)
        x2 = ((b*(-1)) - math.sqrt(delta))/(2*a)
        print('x1=%f; x2=%f' % (x1, x2))
        return x1, x2

print('一元两次方程式求解（aX^2 + bX + c = 0）')
a = float(input('请输入a：'))
b = float(input('请输入b：'))
c = float(input('请输入c：'))
print(quadratic(a, b, c))

###
#print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
#print(quadratic(1, 3, -4))  # => (1.0, -4.0)