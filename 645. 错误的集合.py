class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        # print(nums)
        same = 0
        lost = 0
        n = [0]*(len(nums)+1)
        for c in nums:
            n[c] += 1
        f1, f2 = True, True
        for i in range(1, len(n)):
            if n[i] == 0:
                lost = i
                f1 = False
            if n[i] == 2:
                same = i
                f2 = False
            if f1 == False and f2 == False:
                break
        # print([same, lost])
        return [same, lost]







if __name__ == '__main__':
    Solution().findErrorNums([3,2,3,4,6,5])
