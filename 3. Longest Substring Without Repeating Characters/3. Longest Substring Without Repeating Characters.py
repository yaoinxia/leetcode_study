class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        curmax = 0
        subStr = ""
        #索引
        i = 0
        length = len(s)
        while i < length:
            #找到当前字符的位置,看subStr中是否存在
            ind = subStr.find(s[i])
            if ind == -1:
                subStr+=s[i]
                curmax += 1

            else:
                if maxLen < curmax:
                    maxLen = curmax
                i = i - len(subStr) + ind
                subStr = ""
                curmax = 0
            i += 1
        if maxLen < curmax:
            maxLen = curmax
        return maxLen

if __name__ == "__main__":
    s1 = "abccc"
    print(Solution().lengthOfLongestSubstring(s1))