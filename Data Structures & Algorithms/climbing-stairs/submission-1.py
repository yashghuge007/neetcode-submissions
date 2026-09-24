class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n
        # dp = [0]*n
        # dp[0] = 1
        # dp[1] = 2
        prev = 1
        curr = 2
        for i in range(2,n):
            # dp[i] = dp[i-1]+dp[i-2]
            curr = curr+prev
            prev = curr-prev
        return curr #dp[-1]