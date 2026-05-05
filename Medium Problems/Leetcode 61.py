# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        total_len = 1
        temp = head
        while temp.next:
            total_len += 1
            temp = temp.next
        act = k % total_len
        if not act:
            return head
        temp = head
        for i in range(act):
            temp = temp.next
        
        new_head = head.next
        prev = head
        while temp.next:
            temp = temp.next
            new_head = new_head.next
            prev = prev.next
        temp.next = head
        head = new_head
        prev.next = None
        return head