class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lstr = []
        for c in s:
            lstr.append(c)
        lstr.reverse()
        #print(''.join(lstr))
        return ''.join(lstr)

if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseString(s))