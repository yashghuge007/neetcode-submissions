class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1:
            return False
        graph = defaultdict(list)
        for i, j in edges:
            if i == j:
                return False
            else:
                graph[min(i,j)].append(max(i,j))
                
        q = deque()
        q.append(0)
        visited=set()
        visited.add(0)
        while q:
            n = len(q)
            while n>0:
                i = q.popleft()
                for nei in graph[i]:
                    if nei in visited:
                        return False
                    q.append(nei)
                    visited.add(nei)
                n-=1
        return True