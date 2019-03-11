#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

if __name__ == '__main__':

    s = sys.stdin.readline().strip()
    l0 = list(map(int, s.split()))
    # print(l0[0])
    # print(l0[1])
    step = 0
    # 定义一个词典key: 坐标， value : 金额
    d = {}
    l = []
    while step < int(l0[0]):
        s1 = sys.stdin.readline().strip()
        l1 = list(map(int, s1.split()))
        print(l1)
        l.append(l1[0])
        d[l1[0]] = l1[1]
        step += 1
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            sum0 = d[i] + d[j]
            if sum0 > maxS:
                maxS = sum0
    print(maxS)
    # print(l)
    # print(d)

