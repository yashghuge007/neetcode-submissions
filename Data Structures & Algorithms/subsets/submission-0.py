class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def back(i):
            if i>=len(nums):
                ans.append(sub[:])
                return
            
            sub.append(nums[i])
            back(i+1)
            sub.pop()
            back(i+1)
        
        back(0)
        return ans