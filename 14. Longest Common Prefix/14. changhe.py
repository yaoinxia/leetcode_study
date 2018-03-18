class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num = int(len(strs))
        min = 0
        result = ""
        if num <= 0:
            return result
        else:
            One = int(len(strs[0]))
            for k in range(num - 1):
                min = One
                I = int(len(strs[k]))
                if min >= I:
                    min = I
            for i in range(min - 1):
                one = strs[0]
                for j in range(num - 1):
                    other = strs[j]
                    if one[i] == other[i]:
                        result = result + one[i]
                    else:
                        break
            return result

s = Solution()
print(s.longestCommonPrefix(['ab', 'abc', 'abccc']))
