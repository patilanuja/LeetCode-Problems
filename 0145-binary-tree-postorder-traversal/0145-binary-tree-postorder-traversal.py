# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        sol = []
        bag = [root]

        while bag:
            node = bag.pop()
            sol.append(node.val)

            if node.left:
                bag.append(node.left)

            if node.right:
                bag.append(node.right)
        return sol[::-1]