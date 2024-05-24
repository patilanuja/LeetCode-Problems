# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)
        counter = 1
        ans = []

        while q:

            size = len(q)
            level = []

            for _ in range(size):

                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:

                if counter % 2 != 0:
                    ans.append(level)
                else:
                    ans.append(level[::-1])

            counter += 1

        return ans