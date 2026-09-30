class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        ans = 0
        
        while r<len(prices):
            profit = prices[r]-prices[l]
            
            if profit>0: #increase window with lower buy
                ans = max(ans,profit)
            else: # next lower buy found, update window here onwards
                l=r
            
            r+=1
        
        return ans