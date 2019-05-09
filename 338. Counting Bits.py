#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    # 使用函数bin直接转换
    def countBits(self, num):
        l = []
        for c in range(num+1):
            c = list(bin(c))
            t = 0
            for i in c:
                if i == '1':
                    t += 1
            l.append(t)
        return l

    def countBits2(self, num):
        dp = [0]
        i = 0
        while True:
            for j in range(1<<i, 1<<(i+1)):
                print(j)
                if j > num:
                    return dp
                dp.append(1+dp[j-(1<<i)])
            i += 1
        return dp



if __name__ == '__main__':
    num = 5
    n = Solution().countBits2(num)
    print(n)
