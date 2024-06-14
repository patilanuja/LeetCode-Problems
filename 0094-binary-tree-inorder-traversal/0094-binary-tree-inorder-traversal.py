# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []
        
        sol = []
        bag = []

        while bag or root:

            while root:
                bag.append(root)
                root = root.left

            root = bag.pop()
            sol.append(root.val)
            root = root.right

        return sol