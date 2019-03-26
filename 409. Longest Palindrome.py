#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思路：使用字典存储，key:字符，value：字符的个数
        dic = {}
        # 1.初始化字典
        for c in s:
            dic[c] = 0
        for c in s:
            dic[c] += 1
        l = list(dic.values())
        print(l)
        # 2. 依次遍历列表中每一个元素，取模2的余数, 如果一旦出现一个奇数，temp=1
        temp = 0
        for n in l:
            if n % 2 == 1:
                temp = 1
        # 3. 遍历列表，取模2后的整数部分
        # 3.1 初始化
        sum0 = 0
        for r in l:
            sum0 += (r//2) * 2
        print(sum0+temp)
        return sum0 + temp

if __name__ == '__main__':
    s = "abccbccdda"
    Solution().longestPalindrome(s)