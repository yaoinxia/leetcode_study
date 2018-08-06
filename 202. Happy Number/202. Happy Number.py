class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num__dict = {}
        while True:
            num__dict[n] = True
            sum = 0
            while n>0:
                sum += (n%10) ** 2
                n = n // 10
            if sum == 1:
                return True
            elif sum in num__dict:
                return False
            else:
                n = sum

if __name__ == "__main__":
    n = Solution().isHappy(19)
    print(n)