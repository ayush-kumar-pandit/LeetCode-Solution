# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root.left and not root.right and low <= root.val <= high:
            return root.val

        res = 0
        st = []
        temp = root

        while temp or st:
            if not temp and st:
                temp = st.pop()
            
            if low <= temp.val <= high:
                res += temp.val

            if temp.right:
                st.append(temp.right)

            temp = temp.left
        return res