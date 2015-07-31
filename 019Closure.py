#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()  # 返回的函数并没有执行
# f1()加上括号调用才是执行函数
# 执行时闭包内部的i已经是3了，所以执行结果都等于9
print(f1())
print(f2())
print(f3())

"""
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量, 方法是再创建一个函数，
用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
已绑定到函数参数的值不变.
"""
def new_count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = new_count()
print(f1())
print(f2())
print(f3())
