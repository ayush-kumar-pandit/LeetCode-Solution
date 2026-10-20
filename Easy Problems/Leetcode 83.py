# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        if not head.next:
            return head
        prv = head
        cur = head.next
        while cur:
            if cur.val == prv.val:
                prv.next = cur.next
                cur = cur.next
            else:
                cur = cur.next 
                prv = prv.next
        return head