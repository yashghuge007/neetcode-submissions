class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dt = [(0,1),(0,-1),(-1,0),(1,0)]

        m,n = len(grid),len(grid[0])

        def dfs(i,j) -> int:
            if i>=m or i<0 or j>=n or j<0 or grid[i][j]==0:
                return 0
            
            grid[i][j]=0
            area = 1
            for r,c in dt:
                area+=dfs(i+r,j+c)
            
            return area
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    ans = max(ans,dfs(r,c))
        return ans