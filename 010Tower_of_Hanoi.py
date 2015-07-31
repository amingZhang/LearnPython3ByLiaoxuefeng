#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

print("汉诺塔游戏")
print('*' * 20)

count = 0

def move(n, a, b, c):
    global count
    if n == 1:
        count += 1
        print(a, "-->", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

while True:
    count = 0
    number = int(input('输入盘子的数目：'))
    move(number, 'A', 'B', 'C')
    print('移动了%d次' % count)
    print("*"*20)