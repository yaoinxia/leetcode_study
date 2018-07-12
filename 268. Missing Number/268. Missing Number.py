class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min = nums[0]
        max = nums[len(nums)-1]
        if len(nums) == max-min+1:
            if min == 0:
                return max+1
            else:
                return 0
        #print(min)-0
        #print(max)-1
        j = 0
        for i in range(min, max+1):
            if nums[j] != i:
                return i
            else:
                j += 1


if __name__ == "__main__":
    nums =[1,2]
    print(0^1)
    print(Solution().missingNumber(nums))