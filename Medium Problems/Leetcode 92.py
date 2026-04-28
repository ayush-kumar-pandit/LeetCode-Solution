# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        ls = []
        temp = head
        while temp:
            ls.append(temp.val)
            temp = temp.next

        l = left - 1
        r = right - 1
        while l < r:
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r -= 1
        temp = head

        for i in ls:
            temp.val = i
            temp = temp.next
        return head        