#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        #将数值赋给i,完成稍后的递减操作
        i = n
        #i只要不为零，就一直减，减1或者2
        while i > 0:
            if i == 1:
                return 1
            else:
                




s = Solution()
s.climbStairs(3)
