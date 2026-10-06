class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        choosen = [False]*len(nums)

        def dfs(temp):
            if len(nums)==len(temp):
                ans.append(temp[:])
                return
            
            for i,v in enumerate(choosen):
                if v == False:
                    temp.append(nums[i])
                    choosen[i]=True
                    dfs(temp)
                    temp.pop()
                    choosen[i]=False
                    # dfs(i+1)
        dfs([])
        return ans
            