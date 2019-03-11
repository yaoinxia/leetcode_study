#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    # 按照从大到小排序
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # print(nums[len(nums)-k])
        return nums[len(nums)-k]

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    Solution().findKthLargest(nums, k)
