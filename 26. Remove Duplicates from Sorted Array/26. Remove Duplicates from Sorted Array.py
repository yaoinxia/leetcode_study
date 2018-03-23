#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i = j
                j = j+1
        return len(nums)
s = Solution()
print(s.removeDuplicates([1,1,2,2,3,3,3,11,11,13,13,44,44]))