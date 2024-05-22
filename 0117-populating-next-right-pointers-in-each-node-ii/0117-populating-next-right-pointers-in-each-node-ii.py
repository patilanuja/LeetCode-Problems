"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        head = root

        while head:
            
            dummy = Node(0)
            temp = dummy

            while head:
                # Connect childs
                if head.left:
                    temp.next = head.left
                    temp = temp.next

                if head.right:
                    temp.next = head.right
                    temp = temp.next
                # move to next element on same level
                head = head.next

            # move on to next level
            head = dummy.next

        return root

