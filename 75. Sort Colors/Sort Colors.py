#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        return nums

    # 使用计数排序的思想
    def sortColors2(self, nums):
        c0 = c1 = c2 = 0
        for c in nums:
            if c == 0:
                c0 += 1
            if c == 1:
                c1 += 1
            if c == 2:
                c2 += 1
        nums = [0] * c0 + [1] * c1 + [2] * c2
        # print([0] * c0 + [1] * c1 + [2] * c2)
        print(nums)
        return [0]*c0 + [1]*c1 + [2]*c2

if __name__ == '__main__':
    Solution().sortColors2(nums=[2,0,2,1,1,0])