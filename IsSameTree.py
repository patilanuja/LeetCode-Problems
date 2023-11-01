################################################# Depth First Search ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(d = depth of the tree) ##########

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        

        stack1, stack2 = [p], [q]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 and node2:
                if node1.val != node2.val:
                    return False
                stack1.append(node1.left)
                stack1.append(node1.right)
                stack2.append(node2.left)
                stack2.append(node2.right)
            elif node1 or node2:
                return False
                
        return True
    

################################################# Recursion ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(h = height of the tree) ##########

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not q and not p: return True

        if p and q and p.val == q.val:
            return (self.IsSameTree(p.left, q.left) and self.IsSameTree(p.right, q.right))
        
