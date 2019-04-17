#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def find_minima(n, m):
    # print(m[0][1])
    # print(len(m[0]))
    # row = len(m)
    # col = len(m[0])
    l = []
    for i in range(0, n):
        for j in range(0, n):
            # 四个顶角考虑下
            # if i == 0 and j == 0:
            #     if m[i][j] < m[i+1][j] and m[i][j]<m[i][j+1]:
            #         l.append(m[i][j])
            # if i == n-1 and j == 0:
            #     if m[i][j] < m[i-1][j] and m[i][j]<m[i][j+1]:
            #         l.append(m[i][j])
            # if i == 0 and j == n-1:
            #     if m[i][j] < m[i+1][j] and m[i][j]<m[i][j-1]:
            #         l.append(m[i][j])
            # if i == n-1 and j == n-1:
            #     if m[i][j] < m[i-1][j] and m[i][j]<m[i][j-1]:
            #         l.append(m[i][j])
            # if i == 0 and j != 0:

            if (i==0 or m[i][j]<m[i-1][j]) \
                and (i+1>n-1 or m[i][j] < m[i+1][j]) \
                and (j==0 or m[i][j]<m[i][j-1]) \
                and (j+1>n-1 or m[i][j] < m[i][j+1]):
                l.append(float(m[i][j]))
    l.sort()
    print(l)





if __name__ == '__main__':
    n = 3
    m = [[1,2,3],
         [4,1,6],
         [7,0,9]]
    find_minima(n, m)