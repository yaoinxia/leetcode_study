#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def countSubstrings(self, s):
        # 先用最普通的方法来写
        if len(s) == 1:
            return 1
        num = 0
        if len(s) < 1000:
            if self.judge_pali(s):
                num += 1
            for win in range(1, len(s)):
                for i in range(0, len(s)-win+1):
                    ss = s[i:i+win]
                    print(ss)
                    if self.judge_pali(s[i:i+win]):
                        num += 1
        return num

    def judge_pali(self, s):
        s = list(s)
        s_r = list(reversed(s))
        # print(s_r)
        for i in range(0, len(s)):
            if s[i] == s_r[i]:
                continue
            else:
                break
        if i == len(s) - 1:
            return True

    # 暴力法，借鉴网上
    def countS(self, s):
        count = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        return count

    # 动态规划的思想


if __name__ == '__main__':
    t = Solution().countS(s="aaa")
    print(t)