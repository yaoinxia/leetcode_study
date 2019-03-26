#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 思路： 蛮力法，直接存储到一维列表中
        # print(matrix[0][1])
        # 定义一维列表，存储数据
        l = []
        if len(matrix) == 1:
            print(matrix[0][0])
            return matrix[0][0]
        # 存储行和列
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                l.append(matrix[r][c])
        print(l)
        l.sort()
        print(l[k-1])
        return l[k-1]


if __name__ == '__main__':
    ma = [
           [1]
        ]
    k = 1
    Solution().kthSmallest(ma, k)