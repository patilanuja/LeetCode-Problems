# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.depth(root)
        return self.dia


    def depth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.depth(root.left)
        right = self.depth(root.right)
        self.dia = max(self.dia, left+right) #Update the diameter
        return (left if left>right else right) + 1 # return the height