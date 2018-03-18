class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        j = 1
        temp = []
        for i in strs[0][i]:
            temp.append(i) = strs[0][i]
            for j in strs[j][i]:
                if temp[i] == strs[j][i]:
                    continue
                else:
                    return temp
        return temp



s = Solution()
print(s.longestCommonPrefix(['ab', 'abc', 'abccc']))
