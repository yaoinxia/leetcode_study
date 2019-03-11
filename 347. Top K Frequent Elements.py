#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 使用桶排序的思想

        # 1. 定义一个桶， 初始化为0
        tub = [0]*(max(nums)+1)
        # 2.如果nums的长度为1，直接输出

        if len(nums) == 1:
            return nums
        for c in nums:
            tub[c] += 1
        print(tub)
        j = 0
        l = []
        while j < k:
            l.append(tub.index(max(tub)))
            j += 1
            tub[tub.index(max(tub))] = 0
        print(l)
        return l

if __name__ == '__main__':
    nums = [1,1,1,2,2,3333333]
    k = 2

    Solution().topKFrequent(nums, k)