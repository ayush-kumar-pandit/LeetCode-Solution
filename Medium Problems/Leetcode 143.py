# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        temp = head
        while temp:
            st.append(temp.val)
            temp = temp.next

        l = 0
        r = len(st) - 1
        temp = head

        while l < r:
            temp.val = st[l]
            temp = temp.next
        
            temp.val = st[r]
            temp = temp.next

            l += 1
            r -= 1
        if l == r:
            temp.val = st[l]