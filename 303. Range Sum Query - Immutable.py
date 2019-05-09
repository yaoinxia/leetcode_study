#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class NumArray:
    def __init__(self, nums):
        self.sums =[0]*(len(nums)+1)
        # 求解第一个元素到该元素的和
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
        return self.sums[j+1] - self.sums[i]

if __name__ == '__main__':
    nums =  [-2, 0, 3, -5, 2, -1]
    print(NumArray(nums).sumRange(0, 2))