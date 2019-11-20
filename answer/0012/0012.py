"""
**第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

def gen_sensitive_words(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(),lines))

input_word = input('请输入词汇：')
for word in gen_sensitive_words(r'..\0011\filtered_words.txt'):
    if word in input_word:
        input_word=input_word.replace(word,'*'.ljust(len(word),'*'))
        print(input_word)
        exit(0)
print('Human Rights')