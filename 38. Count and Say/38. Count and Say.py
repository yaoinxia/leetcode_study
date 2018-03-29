#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        if n == 1:
            return result
        i = 0
        count = 0
        r = ''
        while n > 1:
            while i < len(result) - 1:
                if result[i] != result[i + 1]:
                    r = r + str(i + 1 - count) + result[i]
                    count = i + 1
                i = i + 1
            result = r + str(len(result) - count) + result[-1]
            n = n - 1
            i = 0
            count = 0
            r = ''
        return result





