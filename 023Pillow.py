#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

from PIL import Image

im = Image.open('Test.PNG')  # 文件名大小写敏感
im.show()
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))  # 生成缩略图
im.save('thumb.jpg', 'JPEG')
