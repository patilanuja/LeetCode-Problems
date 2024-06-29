class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.connections = n
        
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        
        if rootX == rootY:
            return True
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
            
        else:
            self.root[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
            
        self.connections -= 1
        return False
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
            
        return uf.connections
        