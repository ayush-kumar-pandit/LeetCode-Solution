# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head.next
        summ = 0
        newList = ListNode()
        temp = newList
        while tail:
            if tail.val:
                summ += tail.val
            else:
                temp.next = ListNode(summ)
                temp = temp.next
                summ = 0
            tail = tail.next
        return newList.next
