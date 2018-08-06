class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #重新赋值
        k = k % len(nums)
        nums[:k] = nums[len(nums)-k:]
        nums[k:] = nums[:len(nums) - k]
        print(nums)

if __name__ == "__main__":
    n = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(n, k)