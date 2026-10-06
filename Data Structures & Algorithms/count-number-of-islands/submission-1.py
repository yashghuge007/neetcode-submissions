class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        delta = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == '0':
                return

            grid[i][j]='0'
            
            for r,c in delta:
                dfs(i+r,j+c)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    ans+=1
                    dfs(r,c)
        return ans