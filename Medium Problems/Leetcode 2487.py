# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        st = []
        temp = head

        while temp:
            st.append(temp.val)
            temp = temp.next
        
        res = []
        x = 0
        for i in range(len(st) - 1, -1, -1):
            if st[i] >= x:
                res.append(st[i])
                x = st[i]
        
        nl = ListNode()
        temp = nl
        for i in range(len(res) - 1, -1, -1):
            
            temp.next = ListNode(res[i])
            temp = temp.next
        return nl.next