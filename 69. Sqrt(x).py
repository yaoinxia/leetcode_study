#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分查找法的思想
        if x <= 1:
            print(x)
            return x
        # 1. 定义一个数字h,专门用来存放除以2的数
        left, right = 0, x
        while left <= right:
            h = (left + right) // 2
            # print(h)
            if x // h < h:
                right = h - 1
            elif x // h > h:
                left = h + 1
            elif x // h == h:
                print(h)
                return h
                break
        print(right)
        return right

if __name__ == '__main__':
    Solution().mySqrt(x=17)

    # print(math.floor(0 + (8 - 0) / 2))
    # print(8//1)