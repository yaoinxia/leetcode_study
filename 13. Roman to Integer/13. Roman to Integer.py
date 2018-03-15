#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        for i in range(len(s) - 1):
            if a[s[i]] < a[s[i + 1]]:
                sum -= a[s[i]]
            else:
                sum += a[s[i]]
        return sum + a[s[len(s) - 1]]


s = Solution()
print(s.romanToInt('IXL'))
