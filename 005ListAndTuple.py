#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __author__ = 'zhang.c.m'

print('现在测试List')
print('*'*20)

testList = []
while True:
    item = input('输入你希望添加的元素：(输入x表示退出)')
    if item == 'x':
        break
    testList.append(item)

listLength = len(testList)
print('你输入的List的元素个数是：%d' % listLength)
for i in range(listLength):
    print('第%d个元素是：' % i + testList[i])

print('\n' + '*'*20)
print('利用pop()函数删除指定的元素')
while True:
    listLength = len(testList)
    index = int(input('请输入下标%d ~ %d：(0表示第一个元素，-1表示最后的元素)' % (listLength*-1, listLength-1)))
    if listLength*-1 <= index < listLength:
        print('删除元素：' + testList[index])
        testList.pop(index)
        print('新的List是：%s' % testList)
    else:
        print('输入错误')
        break

print('\n' + '*'*20)
print('现在测试Tuple')
print('*'*20)
print('Tuple是不可变数组，但是如果其包含的元素是可变元素，则该元素可以变更')
testTuple = ('a', 'b', ['A', 'B'])
print(testTuple)
replaceStr = input('输入想替换A的字符：')
testTuple[2][0] = replaceStr
print(testTuple)
replaceStr = input('输入想替换B的字符：')
testTuple[2][1] = replaceStr
print(testTuple)