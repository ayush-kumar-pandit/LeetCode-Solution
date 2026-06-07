# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        large = dummy
        while large.next and large.next.val < x:
            large = large.next
        small = large.next
        while small and small.next:
            if small.next.val < x:
                temp = small.next.next
                prev = small
                small.next.next = large.next
                large.next = small.next
                large = large.next
                prev.next = temp
            else:
                small = small.next
        return dummy.next
