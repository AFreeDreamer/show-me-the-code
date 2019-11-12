import redis

import string
import random


def genKey(length=20):
    chars=string.ascii_letters+string.digits
    return ''.join(random.choices(chars,k=length))


def getKeys(cnt=10,length=20):
    # keys=[]
    # for i in range(cnt):
    #     keys.append(genKey(length))

    # 直接使用列表推导式
    return [genKey(length) for i in range(cnt)]

ret = getKeys()
r=redis.Redis(host='192.168.57.128', port=6379, db=0, password='password')
# 向redis中插入列表
for i in ret:
    r.lpush('code_l',i)


# r.lpush('code',','.join(ret))
