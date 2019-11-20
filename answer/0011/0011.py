# -*- coding:utf-8 -*-
'''
*第 0011 题：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
	jiangge
'''

"""
思路：

    1、敏感词表读取到列表中
    2、输入内容时，对列表进行匹配
"""

def gen_sensitive_words(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(),lines))

input_word = input('请输入词汇：')
for word in gen_sensitive_words(r'.\filtered_words.txt'):
    if word in input_word:
        print('Freedom')
        exit(1)
print('Human Rights')