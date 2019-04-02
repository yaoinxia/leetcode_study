#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
给定一个表示非负整数的非空数字数组，加上一个整数。
数字被存储为使得最高有效数字位于列表的头部，并且数组中的每个元素都包含单个数字。
您可以假定整数不包含任何前导零，除了数字0本身。
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #print(len(digits))
        index = len(digits)-1
        #print(digits)
        num = 0
        for i in digits:
            if index == -1:
                break
            else:
                #print(i)
                num = i*(10**index)+num
                index -= 1
        num_new = num + 1
        #print(num_new)
        length_new = len(str(num_new))

        num_0 = []
        for i in str(num_new):
            print(i)
            num_0.append(int(i))
        print(num_0)
        return num_0

s = Solution()
s.plusOne([3, 2, 1])
