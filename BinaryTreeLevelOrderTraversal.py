################################################# BFS ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(n no of the nodes) ########### 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: 
            return []

        q = deque([root])
        res = []

        while q:
            temp = []

            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)

                if node.left != None:
                    q.append(node.left)
            
                if node.right != None:
                    q.append(node.right)

            res.append(temp)

        return res
