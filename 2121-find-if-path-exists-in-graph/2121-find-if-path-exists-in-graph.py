class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]

        for s, d in edges:
            adjacency_list[s].append(d)
            adjacency_list[d].append(s)

        stack = [source]
        seen = set()

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node in seen:
                continue

            seen.add(node)

            for neighbor in adjacency_list[node]:
                stack.append(neighbor)

        return False

            