class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque()
        fresh=0

        def bfs(i,j):
            nonlocal fresh
            if i not in range(m) or j not in range(n) or grid[i][j] != 1:
                return
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
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            k+=1
        
        
        return k if fresh == 0 else -1
