# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        x = root.val
        st = []
        temp = root
        while temp or st:
            if temp.right:
                st.append(temp.right)
            if temp.val != x:
                return False
            temp = temp.left
            if not temp and st:
                temp = st.pop()
        return True 