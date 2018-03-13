#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        answer = 0
        x =num
        if x > 0:
            while x != 0:
                answer = answer * 10 + x % 10
                x = x // 10

            if num == answer:
                return True
            else:
                return False
        elif num == 0:
            return True
        else:
            return False

s = Solution()
#s.reverse(-231)
print(s.isPalindrome(121))
