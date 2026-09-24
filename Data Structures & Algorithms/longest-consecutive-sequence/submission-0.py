class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0

        for n in s:
            if n-1 not in s:
                span = 1
                while n+span in s:
                    span+=1
                l = max(l,span)
        return l
        