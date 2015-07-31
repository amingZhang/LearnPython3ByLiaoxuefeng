#!/usr/bin/env python3
#  In the mac and linux, execute following commands, than you can run *.py
#  $ chmod a+x hello.py <- here give rights
#  ./hello.py <- here execute py file
#
# -*- coding: utf-8 -*-
#上一行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# __author__ = 'zhangchangming'

print('这是一个包含中文字符串的文件')

print('*'*20)
inputString = input('ord()函数获取字符的整数表示, 现在请输入任意一个字符（中英文皆可）：')
if len(inputString) > 1:
    print('输入的字符个数大于一个，将截取第一个字符')
    inputString = inputString[0]
print(inputString+'对应的整数是：%d' % ord(inputString))

print('\n'+'*'*20)
inputString = input('chr()函数把编码转换为对应的字符, 现在请输入一个整数：')
print(inputString+'整数对应的字符是：%s' % chr(int(inputString)))

print('\n'+'*'*20)
inputString = input('现在演示用16进制表示字符串, 请先输入一个整数：')
intNumber = int(inputString)
print(inputString+'整数对应的字符是：%s' % chr(intNumber))
print(inputString+'整数对应的16进制数是：%x' % intNumber)
stringHex = '\\u%x' % intNumber
print('转换成16进制表示的字符串：' + stringHex)

print('\n'+'*'*20)
print('现在演示encode()方法，将str编码为指定的bytes')
inputString = input('请输入一些中文字符：')
bytesUtf8 = inputString.encode('utf-8')
print('对\"%s\"' % inputString + '进行utf-8编码：%s' % bytesUtf8)
strUtf8 = bytesUtf8.decode('utf-8')
print('将utf-8编码的bytes解码成字符串：' + strUtf8)
