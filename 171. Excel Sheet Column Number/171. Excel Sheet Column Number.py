class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        Sum = 0
        length = len(s)
        if length == 0:
            return 0
        for i in range(0, length):
            # print(i)
            # print(length-i-1)
            Sum += pow(26, length-i-1) * (ord(s[i])-64)
        return Sum

if __name__ == "__main__":
    c = "AB"
    print(Solution().titleToNumber(c))