#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


    i = 0
        for j in range(i+1,len(nums)-1):
            if nums[i] == nums[j]:
                del nums[j]

            else:
                continue
    return nums


s = Solution()
print(s.removeDuplicates([1,1,2,2,3,3,3,44,44,3,]))