# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=0, next=head)

        curr = head
        while curr and curr.next:
            d = curr.next.val * 2
            curr.val += d // 10
            curr.next.val = d % 10
            curr = curr.next
        if head.val == 0:
            return head.next
        return head