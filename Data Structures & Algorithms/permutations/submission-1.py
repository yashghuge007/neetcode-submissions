class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp=[]
        choosen = [False]*len(nums)

        def dfs(k):
            if len(nums)==k:
                ans.append(temp[:])
                return
            
            for i,v in enumerate(choosen):
                if v == False:
                    temp.append(nums[i])
                    choosen[i]=True
                    dfs(k+1)
                    temp.pop()
                    choosen[i]=False
        dfs(0)
        return ans
            