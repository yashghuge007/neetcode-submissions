class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num-1 not in s: # which means a new consecutive sequence starts at this number
                length = 1
                while num+length in s:
                    length+=1
                longest = max(longest,length) # keep track of longest length of each sequence
        return longest        