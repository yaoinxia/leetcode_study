class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums[0]
        sublen = int(length/2)
        return nums[sublen]

if __name__ == "__main__":
    nums = [2,2,2,3,3,4]
    print(Solution().majorityElement(nums))