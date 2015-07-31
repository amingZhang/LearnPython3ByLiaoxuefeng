#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhangchangming'

_list1 = [36, 5, -12, 9, -21]
print(sorted(_list1))  # 排序

print(sorted(_list1, key=abs))  # 依绝对值排序

_list2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(_list2))  # 排序，按照ASCII

print(sorted(_list2, key=str.lower))  # 转换成小写字符排序

print(sorted(_list2, key=str.lower, reverse=True))  # 排序结果反转输出

# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))

def by_name(t):
    return t[0]

print(sorted(L, key=by_name))

def by_score(t):
    return t[1]

print(sorted(L, key=by_score, reverse=True))
