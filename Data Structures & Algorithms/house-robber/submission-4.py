class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        5,1,2,10,6,2,7,9,3,1
        5,5
        '''
        n = len(nums)
        if n<2:
            return nums[0]
        dp = [0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])

        for i in range(2,n):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return max(dp[-1],dp[-2])