#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # generator调用next()执行
        # generator中遇到yield关键字，就返回，
        # 再次调用next()从上次yield语句处继续执行
        a, b = b, a+b
        n += 1
    return 'done'

for n in fib(8):
    print(n)
# 用for循环调用generator时，发现拿不到generator的return语句的返回值

# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(8)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print('\n', '*'*20)
print('利用generator生成杨辉三角')

def yanghui_triangles(max_level):
    current_level = 0
    total_arrays = [[1], [1, 1]]
    while current_level < max_level:
        if current_level >= 2:
            previous_list = total_arrays[current_level - 1]
            current_list = [1]
            item = []
            for i, m in enumerate(previous_list):
                if i < len(previous_list) - 1:
                    item.append(m + previous_list[i+1])
            for i in item:
                current_list.append(i)
            current_list.append(1)
            total_arrays.append(current_list)
        yield total_arrays[current_level]
        current_level += 1

# 以下方法是网上学来的，非常简洁的方法
def yanghui_triangles_excellent(max_level):
    a = [1]
    for i in range(max_level):
        yield a
        a = [sum(x) for x in zip([0] + a, a + [0])]
'''以上代码中，
［0］＋a => 等于在a的左面加元素［0］
a＋［0］ => 等于在a的右面加元素［0］
[0] + a => [0, 1]
a + [0] => [1, 0]

zip函数的作用如下：
x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]

xyz = zip(x, y, z)

print xyz
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

***********************************************
所以当a=[1, 2, 1]时，zip([0] + a, a + [0])得到的是

[(0,1), (1, 2),(2, 1), (1,0)]

所以[sum(i) for i in zip([0] + a, a + [0])]等价于
[sum(i) for i in [(0,1), (1, 2),(2, 1), (1,0)]]
'''

for t in yanghui_triangles_excellent(10):
    print(t)

