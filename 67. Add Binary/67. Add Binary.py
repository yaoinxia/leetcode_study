#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_10a = int(a,2)
        int_10b = int(b,2)
        sum_10 = int_10a+int_10b
        sum_2 = bin(sum_10).replace('0b', '')
        print(sum_2)
        return str(sum_2)

s = Solution()
s.addBinary("11","1")