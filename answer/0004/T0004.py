import re
from collections import Counter

# 任一个英文的纯文本文件，统计其中的单词出现的个数。

def getWordsList(filename):
    ret = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        [ret.extend(re.findall(r'[a-zA-Z]+', line)) for line in lines]
    return ret

print(Counter(getWordsList(r'.\words.txt')).most_common(10))

# most_common(n) 返回出现频次最高的n个元素及其次数
