class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1:
            return False
        visited=set()
        graph = defaultdict(list)
        for i, j in edges:
            if i == j:
                return False
            elif i <j:
                graph[i].append(j)
            else:
                graph[j].append(i)
        print(graph)
        
        # def dfs(i):
        #     if i in visited:
        #         return False
        #     if i == n-1:
        #         return True
        #     visited.add(i)
        #     ans = True
        #     for nei in graph[i]:
        #         ans = ans and dfs(nei)
        #     return ans
        
        q = deque()
        q.append(0)
        visited.add(0)
        while q:
            q2 = deque()
            while len(q)>0:
                i = q.popleft()
                for nei in graph[i]:
                    if nei in visited:
                        return False
                    q2.append(nei)
                    visited.add(nei)
            q.extend(q2)
        return True

        # def bfs(i):
        #     if i in q:
        #         return False
        #     if i == n-1:
        #         return True
        #     # q.append(i)
        #     ans = True
        #     for nei in graph[i]:
        #         q.append(nei)
        #     ans = ans and bfs(nei)
        #     return ans
        
        # return bfs(0)