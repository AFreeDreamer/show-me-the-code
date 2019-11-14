import string
import random

'''
    说明：
    功能：
    作者：
    时间：
'''
  
        warnings.warn(
            "The _imaging extension was built for another version of Python.",
            RuntimeWarning,
        )

# keys=[]
# for i in range(cnt):
#     keys.append(genKey(length))

# 直接使用列表推导式
def genKey(length=20):
    # 直接使用列表推导式
    chars=string.ascii_letters+string.digits
    return ''.join(random.choices(chars,k=length))


def getKeys(cnt=10,length=20):
    # 直接使用列表推导式
    for i in range(cnt):
        print(genKey(length))

def getKeys111(cnt=10,length=20):
    """
        参数：
        cnt:10
        length:20
    """
    for i in range(cnt):
        print(genKey(length))

getKeys(cnt=10,length=20)
