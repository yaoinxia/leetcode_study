


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size = len(strs)

        if size == 0:
            return ''
        if size == 1:
            return strs[0]
        ans = strs[0]
        i = 1
        while i < size:
            j = 0
            minlen = min(len(ans), len(strs[i]))
            # print(minlen)
            while j < minlen:
                if ans[j] != strs[i][j]:
                    break
                j += 1
            if j == 0:
                return ''
            ans = ans[:j]
            i += 1
        return ans


