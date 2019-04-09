#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

def find_2(n, k, l):

    if n*[0] == l:
        print(0)
    min_v = min(l)
    # print(l.index(min_v))
    if k == 1:
        for c in l:
            if c == 0:
                del c
        print(min(l))
    elif k > 1:
        tem = 0
        while tem < k:
            for i in range(n):
                if l[i] >= min_v:
                    l[i] = l[i] - min_v
            print(l)
            min_v = min(l)
            print(min(l))
            tem += 1

        print(min_v)


if __name__ == '__main__':
    # n = 2
    # k = 2
    # l0 = [0,0]
    # l = [4, 6]
    # l = [0, 1, 2]

    #
    line1 = sys.stdin.readline().strip()
    values1 = list(map(int, line1.split()))
    # print(values1[0])
    # print(values1[1])

    line2 = sys.stdin.readline().strip()
    values2 = list(map(int, line2.split()))
    # print(values2)
    # print(values2[0])
    # print(values2[1])

    # min_v = min(l)
    # print(min_v)
    find_2(values1[0],values1[1],values2)

