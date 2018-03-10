class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = flag = 0
        for i in range(len(s)):
            if (len(s) - i - 1) < length:
                break
            count, dictx = 0, {}
            # ?
            for c in s[flag:]:
                if not dictx.get(c):
                    dictx[c] = True
                    count += 1
                else:
                    break
            if count > length:
                length, count = count, length
            flag += 1

        return length
