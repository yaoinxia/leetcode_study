#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. 定义一个字典，key：nums中的元素，value：具体索引值
        d = {}
        for i in range(0, len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    Solution().twoSum(nums, target)