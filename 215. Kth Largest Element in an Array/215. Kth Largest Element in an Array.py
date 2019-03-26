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

    # 采用快排的思想
    def findKthLargest2(self, nums, k):
        if len(nums) == 1:
            return nums
        # 选一个对象temp, 默认为nums[0]
        temp = nums[0]
        # 定义left, right 列表
        left = []
        right = []
        for i in range(1, len(nums)):
            if nums[i] < temp:
                left.append(nums[i])
            else:
                right.append(nums[i])
        self.findKthLargest2(left)
        self.findKthLargest2(right)
        return nums

    def quick_sort(self, arr, left, right):
        if left < right:
            t = self.partition(arr, left, right)
            self.quick_sort(arr, left, t-1)
            self.quick_sort(arr, t+1, right)
        print(arr)

    def partition(self, arr, left, right):
        t = left
        for i in range(left+1, right):
            if arr[t] >= arr[i]:
                arr[t], arr[i] = arr[i], arr[t]
                t += 1
        print(t)
        return t

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    # Solution().findKthLargest2(nums, k)
    Solution().quick_sort(nums, 0, 8)