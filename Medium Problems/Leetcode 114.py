# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root:
            temp = root.left
            st = []
            st.append(root.right)
            tail = root
            while temp or st:
                if temp:
                    tail.right = temp
                    tail.left = None
                    tail = tail.right
                    if temp.right:
                        st.append(temp.right)
                    temp = temp.left
                if not temp and st:
                    temp = st.pop()

                
                    