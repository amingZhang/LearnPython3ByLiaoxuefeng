#!/usr/bin/env python3
#  In the mac and linux, execute following commands, than you can run *.py
#  $ chmod a+x hello.py <- here give rights
#  ./hello.py <- here execute py file
# -*- coding: utf-8 -*-
#  特别注意：在终端使用./hello.py直接运行不成功，提示“/usr/bin/env: python3\r: No such file or directory”
#  原因通常是：windows和Linux下回车符号不同引起。windows下用\r\n作为换行，linux下用\n作为换行，多了一个\r导致文件名找不到
#  将python文件的回车符改成LF(\n)形式保存后，再运行即可

name = input("please input your name:")
print('hello,', name)
