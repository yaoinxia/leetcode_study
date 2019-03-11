#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 蛮力法
        # 1.先对两个数组进行排序
        g.sort()
        s.sort()
        # 2.定义一个最终的数，存放最大的数字结果,
        n = 0

        child = 0
        cookies = 0
        while n <= len(s) and child < len(g) and cookies < len(s):
            if g[child] <= s[cookies]:
                n += 1
                child += 1
                cookies += 1
            else:
                cookies += 1



        print(n)
        return n


if __name__ == '__main__':
    g = [1, 2, 3, 4]
    s = [1, 1]
    Solution().findContentChildren(g, s)