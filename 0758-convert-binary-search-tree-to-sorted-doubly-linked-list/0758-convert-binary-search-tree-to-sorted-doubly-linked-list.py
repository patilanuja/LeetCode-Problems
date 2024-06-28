"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None

        def dll(node):
            nonlocal first, last # (making it nonlocal to keep updated values )
            # (another way is to pass them as an argument and return those values at the end)
            
            if not node:
                return None
            
            dll(node.left)

            if last:
                last.right = node
                node.left = last

            else:
                first = node
            
            last = node

            dll(node.right)

        first = last = None

        dll(root)

        
        last.right = first
        first.left = last

        return first

                      