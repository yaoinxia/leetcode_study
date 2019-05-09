#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def minCostClimbingStairs(self, cost):
        # dp存放到达每一层的花费值
        costed = [0, 0]
        for i in range(2, len(cost)):
            costed.append(min(costed[i - 1] + cost[i - 1], costed[i - 2] + cost[i - 2]))
        return min(costed[-1] + cost[-1], costed[-2] + cost[-2])

if __name__ == '__main__':
    t = Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(t)