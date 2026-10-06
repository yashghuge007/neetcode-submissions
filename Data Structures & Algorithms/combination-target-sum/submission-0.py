class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(k,i,cur):
            if k == target:
                ans.append(cur[:])
                return
            
            if i>=len(nums) or k>target:
                return

            cur.append(nums[i])
            dfs(k+nums[i],i,cur)
            cur.pop()
            
            dfs(k,i+1,cur)

        dfs(0,0,[])
        return ans


