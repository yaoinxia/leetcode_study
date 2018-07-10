class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for p in nums:
            if p == 0:
                nums.remove(p)
                nums.append(0)
            else:
                continue
        return nums
if __name__ == "__main__":
    num = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(num))
