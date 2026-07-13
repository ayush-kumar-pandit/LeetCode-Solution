# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prv = dummy
        nxt = head.next
        cur = head
        while cur and cur.next:
            prv.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            prv = cur
            cur = cur.next
            if not cur or not cur.next:
                break
            nxt = cur.next
        return dummy.next
