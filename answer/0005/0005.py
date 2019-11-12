
import glob
from PIL import Image
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# iPhone5 分辨率：1136*640


imgs=glob.glob(r'..\0005\img\*.jpg')
imgs.extend(glob.glob(r'..\0005\img\*.png'))

# 设置iPhone的分辨率
w,h=1136,640

for imgpath in imgs:
    img=Image.open(imgpath)
    # 显示原始图片
    img.show()
    img.thumbnail((w,h))
    # 显示调整后的图片
    img.show()

# 相比image.image.resize(),image.image.thumbnail()不用担心的产生拉伸问题
