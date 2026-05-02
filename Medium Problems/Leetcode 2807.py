# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        cur = head.next
        prev = head
        while cur:
            x = math.gcd(cur.val, prev.val)
            temp = ListNode(x,cur)
            prev.next = temp
            cur = cur.next
            prev = prev.next.next
        return head