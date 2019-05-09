#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        total = 0
        i = 0
        while i < len(nums):
            total += nums[i]
            i += 2
        print(total)
        return total


if __name__ == '__main__':
    num = [1,4,3,2]
    Solution().arrayPairSum(num)
