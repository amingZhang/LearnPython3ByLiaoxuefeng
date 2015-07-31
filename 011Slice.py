#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

print('对List, tuple, str可以进行切片（Slice）操作')
print('*'*20)

list0to10 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
print(list0to10)
print('*'*20)

print('切片语法：[begin:end:step]')
print('[:5]')
print(list0to10[:5])

print('*'*20)
print('[3::3]')
print(list0to10[3::3])

print('*'*20)
print('[-5::-1]')
print(list0to10[-5::-1])

str0to9 = "0123456789"
print('*'*20)
print('str同样操作', str0to9)
print('[2:8:2]')
print(str0to9[2:8:2])