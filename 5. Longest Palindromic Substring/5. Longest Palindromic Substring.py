class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        #起始位置
        first = 0
        #长度
        count = 1
        for k in range(0, len(s)):
            c_temp = 0
            for p in range(len(s)-1, k, -1):
                # 从k开始
                i = k
                # 临时长度设置为c_temp= 0
                print(p)
                if s[i] != s[p]:
                    continue
                j = p
                c_temp = 2
                i += 1
                j -= 1
                while i < j:
                    if s[i] != s[j]:
                        c_temp = 0
                        break
                    else:
                        i += 1
                        j -= 1
                        c_temp += 2
                if i == j:
                    c_temp += 1
                if c_temp > count:
                    count = c_temp
                    first = k
        #print(s[first: count])
        return s[first: first+count]

if __name__ == "__main__":
    s = "babad"
    # print("=======================")
    # print(str(list(s).reverse()))
    #print(s[0: 1])
    print(Solution().longestPalindrome(s))
