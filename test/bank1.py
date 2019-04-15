#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

def find_k(n, m , l):
    # print(l)
    l_s = sorted(l)
    min_v = min(l_s)
    max_v = max(l_s)
    if min_v == max_v:
        print(min_v + m//2 , max_v+m)
    elif (max_v-min_v) >= m:
        print(min_v+1, max_v+m)
    elif (max_v-min_v) < m:
        print(min_v+1, max_v+m)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    l = []
    for i in range(n):
        l.append(int(input()))
    find_k(n,m,l)