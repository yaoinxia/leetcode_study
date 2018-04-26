#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        print(cur)
        return cur


s = Solution()
s.climbStairs(5)
