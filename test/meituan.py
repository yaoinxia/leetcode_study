#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

def change_M(n, m, L):
    l = []
    # n:行
    t = 1
    for i in range(0, n):
        for j in range(0, m):

            # 四个顶角考虑下
            if i == 0 and j == 0:
                if L[i][j] != L[i+1][j] and L[i][j] != L[i][j+1]:
                    if L[i+1][j] != L[i][j+1]:
                        t += 1
            elif i == n-1 and j == 0:
                if L[i][j] != L[i-1][j] and L[i][j] != L[i][j+1]:
                    if L[i-1][j] != L[i][j+1]:
                        t += 1
            elif i == 0 and j == n-1:
                if L[i][j] != L[i+1][j] and L[i][j] != L[i][j-1]:
                    if L[i+1][j] != L[i][j-1]:
                        t += 1
            elif i == n-1 and j == n-1:
                if L[i][j] != L[i-1][j] and L[i][j] != L[i][j-1]:
                    if L[i-1][j] != L[i][j-1]:
                        t += 1
            else:
                if L[i-1][j] == L[i+1][j] and L[i-1] == L[i][j+1] and L[i-1][j] == L[i][j-1] and L[i-1] == L[i][j+1]:
                    if L[i][j] != L[i-1][j]:
                        t += 1
                if L[i-1][j] == L[i+1][j] and L[i-1] == L[i][j+1] and L[i-1][j] == L[i][j-1] and L[i-1] != L[i][j+1]:
                    if L[i][j] != L[i-1][j]:
                        t += 2
                    else:
                        t += 1
                if L[i-1][j] == L[i+1][j] and L[i-1] == L[i][j+1] and L[i-1][j] != L[i][j-1] and L[i-1] == L[i][j+1]:
                    if L[i][j] != L[i-1][j]:
                        t += 2
                    else:
                        t += 1
                if L[i-1][j] != L[i+1][j] and L[i-1] == L[i][j+1] and L[i-1][j] == L[i][j-1] and L[i-1] == L[i][j+1]:
                    if L[i][j] != L[i-1][j]:
                        t += 2
                    else:
                        t += 1
                if L[i-1][j] == L[i+1][j] and L[i-1] != L[i][j+1] and L[i-1][j] == L[i][j-1] and L[i-1] == L[i][j+1]:
                    if L[i][j] != L[i-1][j]:
                        t += 2
                    else:
                        t += 1
    print(t)

if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     print(values)
    #     for v in values:
    #         ans += v
    # print(ans)
    line1 = sys.stdin.readline().strip()
    values = list(map(int, line1.split()))
    n = values[0]
    m = values[1]
    L = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        L.append(values)
    # L = [[1, 2, 3],
    #      [4, 1, 6],
    #      [7, 0, 9]]
    change_M(n,m,L)
