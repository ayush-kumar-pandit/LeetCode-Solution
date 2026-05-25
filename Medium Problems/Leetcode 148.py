# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        if not head or not head.next:
            return head
        tail = head
        while tail:
            ls.append(tail.val)
            tail = tail.next
        ls.sort()
        tail = head
        for i in ls:
            tail.val = i
            tail = tail.next
        return head