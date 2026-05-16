# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return res
        st = []
        node = root
        
        while node or st:
            while node:
                st.append(node)
                res.append(node.val)
                node = node.left
            node = st.pop()
            node = node.right
        return res