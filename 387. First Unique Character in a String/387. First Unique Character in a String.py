
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1

if __name__ == "__main__":
    s = "aadd"
    s1 = "aassd"
    s2 = "loveleetcode"
    #print(Solution().firstUniqChar(s))
    print(Solution().firstUniqChar(s1))
    #print(Solution().firstUniqChar(s2))
