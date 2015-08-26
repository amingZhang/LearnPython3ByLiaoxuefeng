#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhangchangming'

import socket

# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)  # recvfrom()方法返回数据和客户端的地址与端口
    print('Received data=%s from %s:%s.' % (data.decode('utf-8'), addr[0], addr[1]))

    if not data or data.decode('utf-8') == "bye-bye":
        break

#    s.sendto(b'Hello, %s!' % data, addr)  # 服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
    s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)

s.close()
# 注意这里省掉了多线程，因为这个例子很简单
