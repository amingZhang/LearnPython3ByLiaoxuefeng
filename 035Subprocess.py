#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code: ', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ouput, err = p.communicate(b'set q=mx\npythone.org\nexit\n')
print(ouput)  # print(output.decode('utf-8'))
print('Exit code: ', p.returncode)
