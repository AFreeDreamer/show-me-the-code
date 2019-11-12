# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# https://blog.csdn.net/jacky_chenjp/article/details/52268272

import re
from collections import Counter
import glob
import os


def getWordsList(filename):
    ret = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        [ret.extend(re.findall(r'[a-zA-Z]+', line)) for line in lines]
    return ret


def getTxts(path):
    return glob.glob(os.path.join(path, '*.txt'))


def getCnt(wordlist, exclude=None, n=None):
    c = Counter(wordlist)
    if exclude:
        for key in exclude:
            c[key] = 0
    print(c.most_common(n))
    # c=Counter(wordlist)
    # ret=dict(c.most_common())
    # print(ret['is'])
    # if exclude:
    #    {ret.pop(str) for str in exclude}
    # ret.


if __name__ == "__main__":
    path = r'.\txt'
    words = []
    # 列表推导式
    [words.extend(getWordsList(filename)) for filename in getTxts(path)]
    getCnt(words, exclude=['is', 'and'], n=10)
