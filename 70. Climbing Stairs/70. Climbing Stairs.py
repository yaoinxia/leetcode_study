#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
<<<<<<< HEAD
        pre = 1
        ppre = 1
        if n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                tmp = pre
                pre = ppre +pre
                ppre = tmp
            return pre

s = Solution()
s2 = s.climbStairs(3)
print(s2)
=======
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        print(cur)
        return cur


s = Solution()
s.climbStairs(5)
>>>>>>> db95d048ec22e4e8b20889828af31c27449d1f2e
