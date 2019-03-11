#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. 定义一个空列表存放字符串数组
        l_s = []
        for c in s:
            l_s.append(c)
        l_s_set = set(l_s)
        if len(l_s_set) == 1:
            print("True")
            return True
        len_s = len(l_s)
        if len_s % 2 == 0:
            mid = int(len_s / 2)
            for i in range(0, mid):
                if l_s[i] == l_s[mid+i]:
                    continue
                else:
                    print("False")
                    return False
                    break
            if i == mid:
                print("True")
                return True

    def repeatedSubstringPattern2(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        s2 = str + str
        print(s2)
        print(ss)
        return ss.find(str) != -1

if __name__ == '__main__':
    s = "aaabaa"
    Solution().repeatedSubstringPattern2(s)
