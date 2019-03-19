#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    # 参考网上的思路，整个小岛的周长是4×陆地数-2×相交数
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1. num找陆地数
        num = 0
        # 2. neg找相交数
        neg = 0
        M, N = len(grid), len(grid[0])
        # M:行数，N:列数
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    num += 1
                    if i < M - 1:
                        if grid[i+1][j] == 1:
                            neg += 1
                    if j < N - 1:
                        if grid[i][j+1] == 1:
                            neg += 1
        print(4*num-2*neg)
        return 4*num - 2*neg


if __name__ == '__main__':
    grid = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
    Solution().islandPerimeter(grid)
