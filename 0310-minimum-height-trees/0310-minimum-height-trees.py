class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        # Create Adjacency list and degree list
        adj = defaultdict(list)
        degree = [0]*n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1


        # Create queue to store nodes with degree 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining_nodes = n

        # loop till remaining nodes > 2
        while remaining_nodes > 2:

            size = len(q)
            remaining_nodes -= size

            # remove node from q
            for i in range(size):
                node = q.popleft()

                # reduce degree of each node
                for neighbor in adj[node]:
                    degree[neighbor] -= 1

                    # if degree neighbor becomes 1, add it to the q
                    if degree[neighbor] == 1:
                        q.append(neighbor)

        return list(q)

