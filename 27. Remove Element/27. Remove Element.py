#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len1 = len(nums)
        for i in range(len1-1):
            if val == nums[i]:
                del nums[i]
                len1= len1-1
            else:
                continue
        return len1


s = Solution()
print(s.removeElement([1,1,2,2,3,3,3,44,44,3,1],3))

