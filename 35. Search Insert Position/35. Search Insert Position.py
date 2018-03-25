#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            result = nums.index(target)
            return result
        else:
            nums.append(target)
            nums.sort()
            result = nums.index(target)
            return result


s = Solution()
print(s.searchInsert([1,3,5,6], 5))




