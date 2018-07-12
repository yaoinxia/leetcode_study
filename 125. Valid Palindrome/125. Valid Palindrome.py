import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = s.lower()
        #s2 = s1.replace(' ', '')
        if len(s) == 0 or len(s) == 1:
            return True
        s3 = ''.join(re.split(r'[^A-Za-z0-9]', s1))
        length = len(s3)
        i = 0
        j = length-1
        while i < j:
            if s3[i] == s3[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    str0 = "0p,"
    print(Solution().isPalindrome(str0))