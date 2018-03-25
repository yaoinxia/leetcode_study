class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = haystack.find(needle)
        return result

s = Solution()
print(s.strStr("hellqisha","llo"))
