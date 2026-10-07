class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque()
        fresh=0

        def bfs(i,j):
            nonlocal fresh
            if (i in range(m) and j in range(n) and grid[i][j] == 1):
                q.append((i,j))
                grid[i][j] = 2
                fresh-=1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
            
        k = 0
        while fresh>0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                # grid[r][c]=2
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            k+=1
        
        
        return k if fresh == 0 else -1
