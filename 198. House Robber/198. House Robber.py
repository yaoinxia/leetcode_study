class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0], nums[-1])
        #进行记录，为一个列表，初始化，所有元素均为0
        money = [0]*len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i-2], money[i-1])
        return money[len(nums)-1]

if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))