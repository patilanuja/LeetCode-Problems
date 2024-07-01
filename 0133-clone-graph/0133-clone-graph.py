"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def clone(node):

            if node in oldToNew:
                return oldToNew[node]

            new_copy = Node(node.val)
            oldToNew[node] = new_copy

            for neighbor in node.neighbors:
                new_copy.neighbors.append(clone(neighbor))

            return new_copy

        oldToNew = {}
        return clone(node) if node else None