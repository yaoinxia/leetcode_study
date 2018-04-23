#!/usr/bin/env python
# _*_ coding:utf-8 _*_
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
