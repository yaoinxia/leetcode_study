class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        nb = bin(n)[2::1]
        print(nb)
        c = ('0'*(32-len(nb)) + nb)
        print(c)
        i = 0
        for temp in c:
            if temp == '1':
                i += 1
        return i


if __name__ == "__main__":
    n = Solution().hammingWeight(128)
    print(n)
