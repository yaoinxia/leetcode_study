#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 1.先分好词，存在一个字符数组里面
# 2.遍历字符数组，然后遍历停用词数组，在停用词数组里面的，不保留，不在的就存下来
import sys

import os
import jieba

# 分词path:指定停用词路径，text:要分词的文本
# cut_all=True全模式
# cut_all=False全模式
def segment(text):
    textCut = jieba.cut(text, cut_all=False)
    # stopwords = stopwordlist(stopwordsPath)
    result = ''
    print('sucess segment')
    for w in textCut:
        result += w + ' '
    print(result)
    # return result

def segment2(text):
    l_text = list(text)
    le = len
    # 定义概率p
    p = [0 for i in range(le)]
    p[le-1] = 1
    d = [1 for i in range(le)]
    t = [1 for i in range(le)]
    for i in range(le, -1, -1):
        for j in range(le, le-i+1):
            if j > 1 and d[l_text[i:i+j]] == 1:
                continue
            if d[l_text[i:i+j]] * p[i+j]*d[i]>p[i]*d[i+j]:
                p[i]=d[l_text[i:i+j]] * p[i+j]

    print(l_text.encode('utf-8'))


if __name__ == "__main__":
    # 读取第一行的n
    str = sys.stdin.readline().strip()
    # str = "北京大学是北京著名的大学"
    segment2(str)
