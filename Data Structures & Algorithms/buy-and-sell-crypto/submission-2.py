class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP = prices[0]
        maxP = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minP:
                minP = prices[i]
                maxP = prices[i]
            else:
                maxP = prices[i]
                profit = max(profit,maxP-minP)
        return profit
