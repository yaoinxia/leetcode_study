class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxP1 = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxP1 += prices[i] - prices[i-1]
        return maxP1

if __name__ == "__main__":
    pic = [2,1,4,5,2,9,7]
    res = Solution().maxProfit(pic)
    print(res)