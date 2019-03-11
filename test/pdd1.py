#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

def calc(length, l1, l2):
    # 先进行排序
    l1.sort()
    l2.sort()
    sum1 = 0
    for i in range(0, length):
        sum1 += l1[i]*l2[length-1-i]
    print(sum1)

if __name__ == '__main__':
    length = int(sys.stdin.readline().strip())
    # print(length)
    # for line in sys.stdin:
    #     a = line.split()
    #     print(int(a[0]) + int(a[1]))
    v1 = sys.stdin.readline().strip()
    l1 = list(map(int, v1.split()))
    v2 = sys.stdin.readline().strip()
    l2 = list(map(int, v2.split()))
    # print(l1)
    # print(l2)
    l1.sort()
    l2.sort()
    sum1 = 0
    for i in range(0, length):
        sum1 += l1[i] * l2[length - 1 - i]
    print(sum1)
