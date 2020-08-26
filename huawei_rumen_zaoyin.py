"""
下次做题，需要思考，能不能用最少的操作
"""
class Solution:
    def zaoyin(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [1, i, i]  # [个数， 开始， 结束]
            else:
                d[nums[i]][0] += 1
                d[nums[i]][2] = i   # 记录结束
        max_noise = 0   # 最大噪声频率
        for item in d:
            if d[item][0] >= max_noise:
                max_noise = d[item][0]
        min_length = len(nums)
        for item in d:
            if d[item][0] == max_noise and (d[item][2] - d[item][1] + 1) < min_length:
                min_length = d[item][2] - d[item][1] + 1
        return min_length

if __name__ == '__main__':
    nums = [0, 0, 0, 1, 1]
    obj = Solution()
    print(obj.zaoyin(nums))