# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## Approach 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left == root.right == None:
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1
    

    # Approach 2
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth (root)

    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.depth(root.left),self.depth(root.right)) + 1



        
