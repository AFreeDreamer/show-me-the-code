from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random

# 生成字母验证码

"""
思路：
1、新建一个空白图像 240*60(宽高)
2、用随机色彩填充每一个像素
3、用随机字母填充图像
4、模糊处理
"""


def random_char():
    return chr(random.randint(65,90))

def random_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
    # return (random.randint(200,255),random.randint(200,255),random.randint(200,255))


w,h=60*4,60
# 新建 RGB，240*60的纯白色图像
img = Image.new(mode='RGB',size=(w,h),color=(255,255,255))

# 创建字体对象
font = ImageFont.truetype(font=r'C:/windows/fonts/Arial.ttf',size=36)

# 创建draw绘图对象
draw=ImageDraw.Draw(img)

# 按像素点绘制
for x in range(w):
    for y in range(h):
        draw.point(xy=(x,y),fill=random_color())

img.show()

# 绘制文本,4个字符
for i in range(4):
    draw.text(xy=(60*i+12,12),text=random_char(),fill=random_color(),font=font)

img.show()

# 添加模糊滤镜
img = img.filter(ImageFilter.BLUR)

img.show()

