#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def find_long(s):
    # 定义开始，结束索引 start, end, 一个从头开始扫，另一个从尾部开始扫
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] == s[end]:
            s_0 = start
            e_0 = end
            start += 1
            end -= 1


        else:
            start -= 1

def longestPalindrome(s):
    if s == s[::-1]:
        print(s[::-1])
        return len(s)
    maxLen = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            print("=1", s[i - maxLen - 1:i + 1][::-1])
            maxLen += 2
            continue
        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            print("=0", s[i - maxLen - 1:i + 1][::-1])
            maxLen += 1
    return maxLen


if __name__ == '__main__':
    # s = "12ABBA"
    # print(s[::-1])
    # longestPalindrome(s)
    while True:
        try:
            a = input()
            if a:
                print(longestPalindrome(a))

        except:
            break