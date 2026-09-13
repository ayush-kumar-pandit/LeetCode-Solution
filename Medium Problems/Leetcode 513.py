# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = []
        que.append(root)
        res = None
        while que:
            temp = que.pop(0)
            res = temp.val
            if temp.right:
                que.append(temp.right)
            if temp.left:
                que.append(temp.left)
        return res