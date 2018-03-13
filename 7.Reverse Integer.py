class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x = x // 10

        return sign * answer

s = Solution()
#s.reverse(-231)
print(s.reverse(-223242334831))






