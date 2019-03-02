#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 思路1: 不停进行二叉查找

        length = len(numbers)
        # print(length)
        li = []
        if length == 2:
            li = [1, 2]
        if length == 3:
            for i in range(0, length):
                for j in range(i + 1, length):
                    if numbers[i] + numbers[j] == target:
                        li.append(i + 1)
                        li.append(j + 1)
        mid = length // 2
        # print(mid)
        if length > 3:
            while target < numbers[mid]:
                last = mid
                mid = last // 2
                print(mid)
            # print(mid)

            for i in range(0, mid+1):
                for j in range(i+1, mid+1):
                    if numbers[i] + numbers[j] == target:
                        li.append(i+1)
                        li.append(j+1)
                        break
            # print(li)
            for i in range(mid, length):
                for j in range(i+1, length):
                    if numbers[i] + numbers[j] == target:
                        li.append(i+1)
                        li.append(j+1)
                        break
        print(li)
        return li

    def twoSum2(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start < end:
            s = nums[start] + nums[end]
            if s > target:
                end -= 1
            elif s < target:
                start += 1
            else:
                return (start + 1, end + 1)

if __name__ == '__main__':
    l = [-1, 0]
    t = -1
    Solution().twoSum2(l, t)
