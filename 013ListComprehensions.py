#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

print('List Comprehensions可以方便的生成各种List')
print('*'*20)

print('利用range(0:10:2)生成简单的List')
print(list(range(0,10,2)))

print('*'*20)
print('复杂的应用：')
print('[x * x for x in range(1, 11) if x % 2 == 0]')
print('以上语句中：x * x是循环体中的执行语句')
print('          ：for x in range(1, 11)是循环控制语句')
print('          ：if x % 2 == 0是执行语句的条件')
print('执行结果如下：')
print([x * x for x in range(1, 11) if x % 2 == 0])

print('*'*20)
print('使用两层循环，可以生成全排列')
print('[m + n for m in \'ABC\' for n in \'XYZ\']')
print([m + n for m in 'ABC' for n in 'XYZ'])

print('*'*20)
print('列出当前目录下的所有文件和目录名')
import os
print('[d for d in os.listdir(\'.\')]')
print([d for d in os.listdir('.')])

print('*'*20)
print('最后把一个list中所有的字符串变成小写')
L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1)
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)