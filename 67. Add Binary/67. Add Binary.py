#!/usr/bin/env python
# _*_ coding:utf-8 _*_

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
        sum_2 = bin(sum_10).replace('0b','')
        return str(sum_2)
        print((sum_2))


s = Solution()
s.addBinary("11","1")