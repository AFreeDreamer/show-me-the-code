# -*- coding: utf-8 -*-
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# 思路：https://www.cnblogs.com/chen0427/p/5732245.html

import glob
import os
import re


def getFiles(dir):
    return glob.glob(os.path.join(dir, '*.py'))


def sourceStat(filename):
    d = {'totalline':0,'blankline':0,'commentline':0,'codeline':0}
    with open(filename, 'r', encoding='utf-8') as f:
        # readlines会自动去掉文末的一行空行
        lines = list(map(lambda x: x.rstrip('\n').strip(), f.readlines()))
        flag_comment = False
        for line in lines:
            if line.startswith("'''") or line.startswith('"""'):
                flag_comment = not flag_comment
            if not flag_comment and not line.startswith("'''") and not line.startswith('"""'):
                if not line:
                    d['blankline'] += 1
                    continue
                if line.startswith('#'):
                    d['commentline'] += 1
                    continue
                # 既非三引号注释行，又非空白行，也不是#号注释行，排除后剩下就是代码行
                d['codeline'] += 1
            else:
                d['commentline'] += 1

    d['totalline'] = d['blankline']+d['commentline']+d['codeline']
    return d


if __name__ == "__main__":
    dir = r'.\code'
    d_sum={'totalline':0,'blankline':0,'commentline':0,'codeline':0}
    for filename in getFiles(dir):
        file=os.path.basename(filename)
        d=sourceStat(filename)
        print('{0}文件的总行数为：{1},空白行数：{2},注释行数：{3},代码行数：{4}'.format(file,d['totalline'],d['blankline'],d['commentline'],d['codeline']))
        d_sum['totalline'] += d['totalline']
        d_sum['blankline'] += d['blankline']
        d_sum['commentline'] += d['commentline']
        d_sum['codeline'] += d['codeline']
    print('所有文件的总行数为：{0},空白行数：{1},注释行数：{2},代码行数：{3}'.format(d_sum['totalline'],d_sum['blankline'],d_sum['commentline'],d_sum['codeline']))
