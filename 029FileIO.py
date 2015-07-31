#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import logging

try:
    with open('./test.txt', 'w') as f:
        f.write('hello, world!\n')
        for i in range(10):
            f.write('line: %d\n' % i)
except Exception as e:
    logging.exception(e)

try:
    with open('./test.txt', 'r') as f:
        print(f.read())
except Exception as e:
    logging.exception(e)

try:
    f = open('./test.txt', 'r')
    lines = f.readlines()
    print(lines)
except Exception as e:
    logging.exception(e)
finally:
    if f:
        f.close()  # 如果没有使用with语句，就需要手动close文件

print('\n' + '*'*20)
# StringIO内存中读写str
from io import StringIO
strio = StringIO()
strio.write('hello')
strio.write(' ')
strio.write('world!')
print(strio.getvalue())
strio.close()

strio = StringIO('Hello\nHi\nGoodbye\n')
while True:
    s = strio.readline()
    if s == '':
        break
    print(s.strip())
strio.close()

# BytesIO内存中读写bytes
from io import BytesIO
bytesio = BytesIO()
bytes_code = '中文'.encode('utf-8')
bytesio.write(bytes_code)
print(bytesio.getvalue())
bytesio.close()

bytesio = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(bytesio.read())
bytesio.close()
