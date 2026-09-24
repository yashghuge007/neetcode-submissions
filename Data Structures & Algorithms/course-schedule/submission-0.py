class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in prereq:
            graph[u].append(v)
        
        VISITED,VISITING,UNVISITED = 2,1,0
        states = [UNVISITED]*numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
