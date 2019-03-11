#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

if __name__ == '__main__':

    s = sys.stdin.readline().strip()
    l = []
    if len(s) <= 52:
        for i in s:
            l.append(i.lower())
        l.sort()
        # print(l)
        l1 = set(l)
        l2 = list(l1)
        l2.sort()
        print(l2[0])
