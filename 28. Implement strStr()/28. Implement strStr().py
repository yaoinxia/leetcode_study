class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                elif j == len(needle) - 1:
                    return i - len(needle) - 1
                else:
                    j = 0
            else:
                i += 1
        return -1

s = Solution()
print(s.strStr("helloisha","llo"))
