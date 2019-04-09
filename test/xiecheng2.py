#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
def xiecheng2(l):
    l.sort()
    # print(l)
    le = len(l)
    # 所有负数相加
    sum0 = 0
    if l[0] < 0 and l[1] >= 0:
        sum0 = l[0]+l[1]
        print(sum0)
    elif l[0] < 0 and l[1] <= 0:
        for i in range(le):
            if l[i] < 0:
                sum0 += l[i]
        print(sum0)
    elif l[0] >=0:
        sum0 = l[0] + l[1]
        print(sum0)
    # print(sum0)

def xiecheng2_v2(l):
    l = list(set(l))
    print(l)
    # l.sort()
    # # print(l)
    # le = len(l)
    # # 所有负数相加
    # sum0 = 0
    # if l[0] < 0 and l[1] >= 0:
    #     sum0 = l[0]+l[1]
    #     print(sum0)
    # elif l[0] < 0 and l[1] <= 0:
    #     for i in range(le):
    #         if l[i] < 0:
    #             sum0 += l[i]
    #     print(sum0)
    # elif l[0] >=0:
    #     sum0 = l[0] + l[1]
    #     print(sum0)
    # # print(sum0)

if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    # print(line)
    # print(line.split(", "))
    l_str = line.split(", ")
    l_int = []
    for c in l_str:
        l_int.append(int(c))

    # values = list(map(int, line.split()))
    xiecheng2(l_int)
