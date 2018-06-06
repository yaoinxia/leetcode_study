#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

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

s = Solution()
s2 = s.climbStairs(3)
