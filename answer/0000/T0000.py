
# -*- coding:utf-8 -*-

"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

# 网上案例：https://www.jianshu.com/p/a21238b2d2d1?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

from PIL import Image, ImageDraw, ImageFont
import os

os.chdir(os.path.split(os.path.realpath(__file__))[0])

# 图片路径和名称，非工作目录使用绝对路径或相对路径
imagepath = 'lfxx.png'


# 读入图片
im = Image.open(imagepath)

# 获取图片的宽和高
(width, height) = im.size


# 创建Draw对象
draw = ImageDraw.Draw(im)


# 根据图片大小设置字体大小
fontsize = int(min((width, height))/4)
print(fontsize)


# 创建Font对象
font=ImageFont.truetype('arial.ttf', fontsize)

# 填充颜色
fillcolor="#ff0000"

# 图片填充
draw.text((width - fontsize, 0), '1', font = font, fill = fillcolor)

# 保存输出
im.save('r.png')
