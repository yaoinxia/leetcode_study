#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        i=0
        j=1
        while i < len(nums):
            while j < len(nums):
                if nums[i] == nums[j]:
                    del nums[j]
                    j=j+1

                else:
                    j = j + 1
            i = 0
            j = 1
        return nums
'''
        result = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 2):
            if nums[i + 1] == None:
                break
            if nums[i] == nums[i + 1]:
                del nums[i]
        return nums


s = Solution()
print(s.removeDuplicates([1,1,2,2,3,3,3,44,44,3,1]))