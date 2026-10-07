class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()

        def bfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or visited[r][c] or grid[r][c]==-1:
                return
            q.append((r,c))
            visited[r][c] = True
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    bfs(r,c)
        
        p = 0
        while q:
            for i in range(len(q)):
                nx,ny = q.popleft()
                grid[nx][ny]=p
                bfs(nx+1,ny)
                bfs(nx-1,ny)
                bfs(nx,ny+1)
                bfs(nx,ny-1)
            p+=1
    

