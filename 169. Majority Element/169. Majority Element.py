class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        sublen = int(length/2)
        #最多元素的出现次数
        maxNum = 0
        #出现最多的元素
        maxN = 0
        for i in range(0, length):
            sumNums = 0
            for j in range(i+1, length):
                if nums[j] == nums[i]:
                    sumNums += 1
            if sumNums >= sublen and sumNums > maxNum:
                maxNum = sumNums
                maxN = nums[i]
        return maxN

if __name__ == "__main__":
    nums = [2]
    print(Solution().majorityElement(nums))