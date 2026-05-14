# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        s = set()
        tail = head
        while tail:
            if tail not in s:
                s.add(tail)
            else:
                return tail
            tail = tail.next
        return None