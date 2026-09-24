class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque()

        def addToQ(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==-1 or visited[i][j]:
                return
            q.append([i,j])
            visited[i][j]=True

        # add all treasure points to queue to start bfs
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited[i][j]=True
        
        #spread out from treasure one step at a time and add reachable nodes to q
        dist = 0
        while q:
            for i in range(len(q)): #len is calculated once unlike while loop
                r,c = q.popleft()
                grid[r][c] = dist
                addToQ(r,c-1)
                addToQ(r+1,c)
                addToQ(r-1,c)
                addToQ(r,c+1)
            dist+=1

            
