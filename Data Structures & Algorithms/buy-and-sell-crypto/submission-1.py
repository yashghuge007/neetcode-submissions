class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP = prices[0]
        maxP = prices[0]
        for i in range(1,len(prices)):
            if prices[i]>maxP:
                maxP = prices[i]
                profit = max(profit,maxP-minP)
            elif prices[i]<minP:
                minP = prices[i]
                maxP=prices[i]
        return profit
