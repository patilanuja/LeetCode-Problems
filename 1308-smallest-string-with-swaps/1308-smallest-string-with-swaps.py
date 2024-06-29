class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        
        s = list(s)
        nodes = [i for i in range(len(s))]
        size = [1 for i in range(len(s))]

        def find(x):
            if x == nodes[x]:
                return x
            nodes[x] = find(nodes[x])
            return nodes[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                nodes[rooty] = rootx

        for e1, e2 in pairs:
            union(e1, e2)

        rootToComponent = defaultdict(list)

        for i in range(len(s)):
            root = find(i)
            rootToComponent[root].append(i)

        for k, indices in rootToComponent.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)

            for c, i in zip(chars, indices):
                s[i] = c

        return "".join(s)