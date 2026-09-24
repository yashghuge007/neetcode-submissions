class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        n = len(nums)
        m = 0
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return nums[0] if l>=n else nums[l]