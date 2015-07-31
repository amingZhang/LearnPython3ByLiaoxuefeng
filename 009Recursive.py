#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

print('递归函数')
print('*' * 20)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


n = int(input('计算阶乘，输入一个整数：'))
print(fact(n))

print('\n' + '*' * 20)
print("尾递归优化")
"""
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
都只占用一个栈帧，不会出现栈溢出的情况。
"""


def fact_optimize(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


n = int(input('计算阶乘，输入一个整数：'))
print(fact_optimize(n))

"""
遗憾的是，大多数编程语言没有针对尾递归做优化，
Python解释器也没有做优化。
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
"""