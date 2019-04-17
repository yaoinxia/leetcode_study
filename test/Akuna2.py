class Solution:
    def minNumFlip(self, nums, K):
        '''
        :param nums: 字符串
        :param K: 每次翻转的个数
        :return:
        '''
        temp = "+"
        count = 0
        nums = list(nums)  # Python中字符串是不可变类型，即无法直接修改字符串的某一位字符。需要把字符串转换成列表
        for i in range(len(nums)):
            if nums[i] != temp:
                for j in range(K):
                    if (i+j)<len(nums):
                        nums[i + j] = temp  # 重新赋值字符串的某一位字符
                    else:
                        break

                count += 1

        if (i+1)>len(nums):
            # if j<K:
            count = -1
        print(count)
        return count


solution = Solution()
# test1
nums = "-+++++"
print(solution.minNumFlip(nums, 2))

