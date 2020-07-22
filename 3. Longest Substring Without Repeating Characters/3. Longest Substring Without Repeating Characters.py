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

def longSub(s):
    maxlen = 0
    curmax = 0
    subStr = ""
    # 索引
    i = 0
    length = len(s)
    while i < length:
        ind = subStr.find(s[i])
        if ind == -1:
            subStr += s[i]
            curmax += 1
        else:
            if maxlen < curmax:
                maxlen = curmax
            i = i - len(subStr) + ind
            subStr = ""
            curmax = 0
        i += 1
    if maxlen < curmax:
        maxlen = curmax
    return maxlen


# 2020/07/18
"""
思路：
蛮力法
1.设置head， tail指针，定义滑动窗口的起始点和结束点；
2.如果将head，tail所指向的字符串范围存入dict中，如果遍历之后发现dict中已存在，则记录下此时dict长度，并将head定位到tail, tail
继续后移，之前的dict词典，重新赋值。
"""
def longestSub(s):
    head = 0
    # # 初始滑动窗口为1
    # win = 1
    # if len(s) == 1:
    #     return 1
    max_len = 0
    for i in range(0, len(s)):
        d = {}
        for j in range(i, len(s)):
            if s[j] not in d:
                d[s[j]] = 1
                # print(d)
            else:
                if len(d) > max_len:
                    max_len = len(d)
                break
    return max_len


if __name__ == "__main__":
    s1 = " "
    print(Solution().lengthOfLongestSubstring(s1))
    print(longestSub(s1))
