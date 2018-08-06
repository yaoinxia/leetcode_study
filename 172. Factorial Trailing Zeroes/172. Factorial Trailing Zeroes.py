class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n // 5 > 0:
            i += n // 5
            n = n // 5
        #print(i)
        return i

if __name__ == "__main__":
    Solution().trailingZeroes(30)
    print(Solution().trailingZeroes(135))