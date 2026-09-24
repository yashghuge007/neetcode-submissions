class Solution:
    def slave(self,nums):
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3,n):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)

        p1 = self.slave(nums[:n-1])
        p2 = self.slave(nums[1:])
        return max(p1,p2)