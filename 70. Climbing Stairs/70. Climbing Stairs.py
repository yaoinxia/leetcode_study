#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 找规律，斐波那契数列
        pre = 1
        ppre = 1
        if n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                tmp = pre
                pre = ppre +pre
                ppre = tmp
            return pre

    def climbStairs2(self, n):
        # 定义到第i个台阶,可能的情况数
        if n == 1 or n == 2:
            return n
        else:
            dp = [0]*(n+1)
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[-1]




s = Solution()
s2 = s.climbStairs2(5)
print(s2)
