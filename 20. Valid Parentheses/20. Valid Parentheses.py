#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lens = len(s)

        num = 0

        while num < lens:
#i 每次从零开始赋值
            i = 0
            while s[i]+s[i+1] == '()' or s[i]+s[i+1] == '[]' or s[i]+s[i+1] == '{}':
                s[i] = s[i].replace(' ')
                s[i+1] = s[i+1].replace(' ')
                i+=2
                num+=2
            while s[i+2]+s[i+1] == '()' or s[i+2]+s[i+1] == '[]' or s[i+2]+s[i+1] == '{}':
                s[i+2] = s[i+2].replace(' ')
                s[i+1] = s[i+1].replace(' ')
                i += 3
                num += 2
            s.strip()
            if num==lens:
                return True
            else:
                return False


s = Solution()
print(s.isValid('[](){}'))
