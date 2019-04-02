"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划问题
        num = len(nums)  # 列表长度
        if nums == None and num == 0:
            return 0  # 空返回0
        Global = nums[0]  # 全局最优
        Local = nums[0]  # 当前最优
        i = 1
        while i < num:
            Local = max(nums[i], Local + nums[i])
            # 当前最优是指当前的数与包括当前数的和的比较，选择最大的
            Global = max(Local, Global)
            # 全局最优是指当前的当前最优与前一个全局最优的比较，选择最大的一个
            i += 1
        print(Global)
        return Global

s = Solution()
#print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])