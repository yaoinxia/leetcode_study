#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

def split(num, s):
    # num:编码组数量，s: 编码组
    # 定义滑动窗口，初始为0
    win = 0
    # 存放截取之后的每一个字符串
    l = []
    for i in range(0, num):
        l.append(s[win: win+9])
        win += 9
    total_s = ""
    for i in range(0, num):
        if i == num-1:
            if l[i][0] == "1":
                total_s = total_s + l[0][1:9]
            if l[i][0] == "0":
                total_s += total_s + l[0][9:0:-1]
        else:
            if l[i][0] == "1":
                total_s = total_s + l[0][1:9] + ' '
            if l[i][0] == "0":
                total_s += total_s + l[0][9:0:-1] + ' '
    print(total_s)

def split_0(num, s):
    # num:编码组数量，s: 编码组
    # 定义滑动窗口，初始为0
    win = 0
    total = ""
    # 存放截取之后的每一个字符串
    for i in range(0, num):
        if s[win] == "1":
            total += s[win+1:win+9]
            print(total)
            win += 9
        elif s[win] == "0":
            total += s[win + 1:win + 9]
            print(total)
            win += 9


if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    # num0 = 4
    # s0 = "0abcdefgh1abcdefgh1abcdefgh1abcdefgh"
    split(num, s)
