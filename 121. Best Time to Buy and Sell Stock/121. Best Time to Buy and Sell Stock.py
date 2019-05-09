class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxP = 0
        minS = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minS:
                minS = prices[i]
            elif prices[i] - minS > maxP:
                maxP = prices[i] - minS

        return maxP

    def maxP(self, num):
        if len(num) == 0:
            return 0
        dp = [0]*len(num)
        minP = num[0]
        for i in range(0, len(num)):
            dp[i] = max(num[i]-minP, dp[i-1])
            minP = min(minP, num[i])
        return dp[-1]


if __name__ == "__main__":
    pic = [7,1,5,3,6,4]
    # pic0 = Solution().maxProfit(pic)
    pic0 = Solution().maxP(pic)
    print(pic0)