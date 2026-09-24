class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = maxP = prices[0]
        res = 0
        for p in prices:
            if p<minP:
                minP = maxP = p
            else:
                maxP = p
                res = max(res,maxP-minP)
        return res