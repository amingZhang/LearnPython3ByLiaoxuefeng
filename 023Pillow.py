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

######################################
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test_pillow.PNG')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

from PIL import ImageFilter
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
im2.show()

######################################
# 我们用随机颜色填充背景，再画上文字，最后对图像进行模糊，得到验证码图片
from PIL import ImageDraw, ImageFont

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()
'''
如果运行的时候报错：

IOError: cannot open resource
这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：

'/Library/Fonts/Arial.ttf'
'C:\Windows\Fonts\Arial.ttf'

要详细了解PIL的强大功能，请请参考Pillow官方文档：

https://pillow.readthedocs.org/
'''