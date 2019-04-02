"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = s.split(" ")
        print(dic)
        length = dic.__len__()
        print(length)
        i = length-1
        while i > 0:
            if dic[i] != "":
                break
            else:
                i -= 1
                #continue
        print(len(dic[i]))
        return len(dic[i])
s = Solution()
#print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
s.lengthOfLastWord("Hello World!  ")