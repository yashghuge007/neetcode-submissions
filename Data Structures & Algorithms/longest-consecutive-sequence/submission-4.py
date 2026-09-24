class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0

        for n in nums:
            longest = 0
            while n in numset:
                longest+=1
                n+=1
            ans = max(ans,longest)
        return ans