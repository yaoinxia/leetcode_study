---
layout: post
title: "5. Longest Palindromic Substring"
tag: leetcode刷题笔记
---

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

**Example 1:**

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

**Example 2:**

Input: "cbbd"
Output: "bb"

给定一个字符串s，找到s中最长的回文子字符串。 您可以假设s的最大长度为1000。

**例1：**

输入：“babad”
输出：“bab”
注意：“aba”也是一个有效的答案。
**例2：**

输入：“cbbd”
输出：“bb”

**思路：**
判断是否有回文
需要遍历
设置滑动窗口
先设置窗口大小为2，一直到整个字符串的长度。

**网上参考：**
<https://blog.csdn.net/NXHYD/article/details/72357430>

<http://cwind.iteye.com/blog/2232862>

动态规划思想
<https://blog.csdn.net/fuxuemingzhu/article/details/79573621>

回头再思考，一篇很详细的博客：
<https://blog.csdn.net/tuobadon/article/details/78989601>

O(n)复杂度思想
<https://articles.leetcode.com/longest-palindromic-substring-part-ii/>


**看懂的思路：**
>思路二：首先，设置回文子串起始位置first=0，长度count=1。for k循环遍历字符串s，首先设置临时长度c_temp=0。用i=k,然后for j逆向找个s中第一个与是s[i]相等的字符，这是回文子串的结束位置。此时回文子串的临时长度c_temp=2，然后i++，j–。如果i小于j，则继续判断s[i]==s[j]，相等则i++，j–，c_temp+=2，不相等则c_temp=0，同时break。如果i==j，则c_temp+=1.然后判断c_temp与count的大小，决定是否更新count与first。这样直至循环结束。最后，返回s.substr(first,count)。

~~~python
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
~~~
>上述方法超时，循环太多



