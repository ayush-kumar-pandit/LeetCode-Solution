# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ls = []
        temp = head
        while temp != None:
            ls.append(temp.val)
            temp = temp.next
        ls[k - 1], ls[-k] = ls[-k], ls[k - 1]
        temp = head
        for i in ls:
            temp.val = i
            temp = temp.next
        return head