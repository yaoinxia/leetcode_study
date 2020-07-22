#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def minFallingPathSum(self, A):
        # 思路： 每一行先排列，然后选择首元素，即是最小的falling path,
        # 此方法有问题
        total = 0
        for i in range(0, len(A)):
            A[i] = sorted(A[i])
            print(A[i])
            total += A[i][0]
        return total
    def minFallingPathSum2(self,A):
        M, N = len(A), len(A[0])
        dp = [[0]*(N+2) for _ in range(M)]
        for i in range(M):
            dp[i][0] = dp[i][-1] = float('inf')
            for j in range(1, N+1):
                dp[i][j] = A[i][j-1]
        for i in range(1, M):
            for j in range(1, N+1):
                dp[i][j] = A[i][j-1] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        # dp:[[inf, 17, 82, inf], [inf, 18, -27, inf]]
        return min(dp[-1])


if __name__ == '__main__':
    A = [[17,82],[1,-44]]
    t = Solution().minFallingPathSum2(A)
    print(t)