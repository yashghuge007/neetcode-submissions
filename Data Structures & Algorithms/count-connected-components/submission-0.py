class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        A union Find algo problem
        Find parent of each node and union the nodes with same parent
        if already united, do nothing
        decrement unconnected component each time we perform a union
        """
        parent = [i for i in range(n)] # setting parent of each node to be itself stating n distinct comp
        rank = [1] * n #ranking each node as per its lenght/no of childs

        def findParent(node):
            res = node
            while res!=parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1,n2):
            p1,p2 = findParent(n1),findParent(n2)

            if p1==p2:
                return 0
            
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return 1
        
        res = n
        for i,j in edges:
            res -= union(i,j)
        return res