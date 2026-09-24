class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i,n in enumerate(nums):
            print(i,n)
            c = target - n
            if c in l:
                return [l[c],i]
            l[n]=i