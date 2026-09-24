class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n = len(heights),len(heights[0])

        p_que = deque()
        a_que = deque()
        p_seen = set()
        a_seen = set()

        for i in range(m):
            p_que.append((i,0))
            p_seen.add((i,0))
            a_que.append((i,n-1))
            a_seen.add((i,n-1))
        
        for j in range(1,n):
            p_que.append((0,j))
            p_seen.add((0,j))
            a_que.append((m-1,n-1-j))
            a_seen.add((m-1,n-1-j))
             

        def isReachable(q,seen):
            while q:
                i,j = q.popleft()

                for r,c in [[i,j+1],[i-1,j],[i+1,j],[i,j-1]]:
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))
            return seen
        
        p_reachables = isReachable(p_que,p_seen)
        a_reachables = isReachable(a_que,a_seen)

        return list(p_reachables.intersection(a_reachables))