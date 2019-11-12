import string
import random
import mysql.connector


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
print(ret)

conn = mysql.connector.connect(host='192.168.57.128',user='root', password='password', database='test',port=3306)
cur=conn.cursor()
cur.execute('create table t0002(id int primary key,str varchar(50))')

for inx,key in enumerate(ret):
    cur.execute('insert into t0002 values(%s,%s)',[inx,key])

conn.commit()
conn.close()

