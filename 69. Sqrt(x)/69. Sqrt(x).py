#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = math.sqrt(x)
        return int(num)
        print(int(num))

s = Solution()
s.mySqrt(11)
