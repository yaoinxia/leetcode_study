#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def mincostTickets(self, days, costs):
        # dp: 表示旅行到第i天为止， 所需要的最少的旅行价格
        dp = [0] * (days[-1])

        if days[-1] < 8:
            for i in range(1, days[-1]):
                dp[i] = min(dp[i - 1] + costs[0], costs[1])
        elif days[-1]>=8 and days[-1] <= 30:
            for i in range(1, 8):
                dp[i] = min(dp[i-1] + costs[0], costs[1])
            for i in range(8, days[-1]):
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], costs[2])
        else:
            for i in range(1, 8):
                dp[i] = min(dp[i-1] + costs[0], costs[1])
            for i in range(8, 31):
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], costs[2])
            for i in range(31, days[-1]+1):
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
        print(dp)
        return dp[-1]

    def mincostTickets2(self, days, costs):
        req = set(days)
        dp = [0]*(days[-1]+1)
        for i in range(len(dp)):
            if i not in req:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0, i-1)] + costs[0],
                            dp[max(0, i-7)] + costs[1],
                            dp[max(0, i-30)] + costs[2])
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2, 7, 15]
    t = Solution().mincostTickets2(days, costs)
    print(t)