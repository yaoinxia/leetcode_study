class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        len1 = len(str(num))
        print(len1[0])
        return len1


s = Solution()
s.intToRoman(1234)
print(s.intToRoman(1234))
