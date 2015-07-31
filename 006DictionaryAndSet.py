#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __author__ = 'zhang.c.m'

print('现在测试dict')
print('*'*20)

print('请用户输入一张成绩表')
resultsDictionary = {}
numberClassmate = int(input('班级同学数：'))
for i in range(numberClassmate):
    name = input('第%d个同学的名字：' % (int(i)+1))
    result = int(input('成绩：'))
    resultsDictionary[name] = result
print(resultsDictionary)

print('\n'+'*'*20)
name = input('需要修改成绩的同学名字：')
if resultsDictionary.get(name) is None:
    print('找不到这个同学！')
else:
    result = int(input('新的成绩：'))
    resultsDictionary[name] = result
print(resultsDictionary)

print('\n'+'*'*20)
name = input('需要删除的同学名字：')
if name in resultsDictionary:
    resultsDictionary.pop(name)
else:
    print('找不到这个同学！')
print(resultsDictionary)

print('\n'+'*'*20)
print('现在测试set')
print('*'*20)

print('要创建一个set，需要提供一个list作为输入集合')
print('s = set([1, 2, 3])')
s = set([1, 2, 3])
print(s)

print('重复元素在set中自动被过滤')
print('s = set([1, 1, 2, 2, 3, 3])')
s = set([1, 1, 2, 2, 3, 3])
print(s)

print('通过add(key)方法可以添加元素到set中')
print('s.add(4)')
s.add(4)
print(s)

print('重复添加的，不会有效果')
print('s.add(4)')
s.add(4)
print(s)

print('通过remove(key)方法可以删除元素')
print('s.remove(4)')
s.remove(4)
print(s)

print('set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作')
print('s1 = set([1, 2, 3])')
s1 = set([1, 2, 3])
print('s2 = set([2, 3, 4])')
s2 = set([2, 3, 4])
print('与操作 s1 & s2')
print(s1 & s2)
print('或操作 s1 | s2')
print(s1 | s2)
