# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        return self.dfs(root,-inf,inf) # verify root node
        

    def dfs(self, root, left, right):

        if not root: return True

        if not (root.val > left and root.val < right):
            return False

        return self.dfs(root.left, left, root.val ) and self.dfs(root.right, root.val , right )