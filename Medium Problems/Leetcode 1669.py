# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head1 = tail1 = list1
        for i in range(b + 1):
            if i < a - 1:
                head1 = head1.next
            tail1 = tail1.next
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        head1.next = list2
        tail2.next = tail1
        return list1
