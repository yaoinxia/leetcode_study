class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #for i in nums:
            #print(i)
        length = len(nums)
        #滑动窗口大小
        windows = length
        #移动指针
        i = 0
        #和
        sum01 = 0
        #子串的元素x
        for x in nums:
            sum01 = sum01 + x
            min01 = sum01
            if (sum01 < min01):
                min01 = sum01
            else:
                continue
            print(min01)
            i += 1
        #sum_num = sum(nums)
        #print("sum:" + str(sum_num))


s = Solution()
#print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])