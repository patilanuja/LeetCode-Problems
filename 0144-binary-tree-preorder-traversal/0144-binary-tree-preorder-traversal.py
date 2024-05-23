# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.preorder(root, res)

    def preorder(self, root, res):

        if not root: return 

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

        return res
        