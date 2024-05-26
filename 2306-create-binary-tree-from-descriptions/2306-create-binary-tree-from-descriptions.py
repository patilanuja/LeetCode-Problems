# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        val_to_node = {}
        childs = set()

        for parent, child, left in descriptions:

            if parent not in val_to_node:
                val_to_node[parent] = TreeNode(parent)

            if child not in val_to_node:
                val_to_node[child] = TreeNode(child)

            if left == 1:
                val_to_node[parent].left = val_to_node[child]
            else:
                val_to_node[parent].right = val_to_node[child]

            childs.add(child)

        for parent, _, _ in descriptions:

            if parent not in childs: return val_to_node[parent]

        