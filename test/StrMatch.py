#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def string_match(string, sub_str):
    for i in range(len(string) - len(sub_str) + 1):
        index = i  # index指向下一个待比较的字符
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
        if index - i == len(sub_str):
                return i
#如果没有找到，返回-1
    return -1

if __name__ == "__main__":
    print(string_match("aaaaaaadbcbdcbbdc", "adbc"))
