class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(node):
            path.append(node)
            
            if node == len(graph)-1:
                paths.append(path.copy())
                return

            for neighbor in graph[node]:
                dfs(neighbor)
                path.pop()

        paths = []
        path = []

        dfs(0)
        return paths
            
        