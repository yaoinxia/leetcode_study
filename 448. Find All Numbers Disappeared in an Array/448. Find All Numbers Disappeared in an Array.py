#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    # 该思路有问题
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l = []
        # 思路，排序后，如果后一个数等于前一个数，或者后一个数加1等于前一个数，则继续。
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i] or nums[i+1] == nums[i]+1:
                continue
            else:
                for j in range(nums[i]+1, nums[i+1]):
                    l.append(j)
        print(l)
        return l

    # 正负标志位
    def findDisappearedNumbers2(self, nums):
        for i in range(0, len(nums)):
            j = abs(nums[i])-1
            nums[j] = -abs(nums[j])
        print(nums)
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    l = [4, 3, 2, 7, 8, 2, 3, 1]
    Solution().findDisappearedNumbers2(l)
