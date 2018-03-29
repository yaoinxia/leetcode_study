#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def string_match(string, sub_str):
    sub_strLen = len(sub_str)
    strLen = len(string)
    for i in range(strLen):
        if string[i: i+sub_strLen] == sub_str:
            print(i)

if __name__ == "__main__":
    print(string_match("aaaaaaadbcbdcbbdcadbc", "adbc"))


