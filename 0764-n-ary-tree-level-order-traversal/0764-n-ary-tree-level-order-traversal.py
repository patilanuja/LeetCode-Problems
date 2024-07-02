"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return root
        
        queue = deque()
        queue.append(root)
        levels = []
        
        while queue:
            q_size = len(queue)
            level = []
            
            for _ in range(q_size):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    for child in node.children:
                        queue.append(child)
                    
            if level:
                levels.append(level)
                
        return levels