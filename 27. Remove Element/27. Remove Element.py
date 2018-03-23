#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)


s = Solution()
print(s.removeElement([1,1,2,2,3,3,3,44,44,3,1],3))

