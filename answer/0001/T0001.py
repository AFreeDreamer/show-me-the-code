import string
import random


def genKey(length=20):
    chars=string.ascii_letters+string.digits
    return ''.join(random.choices(chars,k=length))


def getKeys(cnt=10,length=20):
    for i in range(cnt):
        print(genKey(length))

getKeys(cnt=10,length=20)


