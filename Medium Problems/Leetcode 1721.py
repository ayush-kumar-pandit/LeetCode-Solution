# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for _ in range(k - 1):
            temp = temp.next
        temp2 = temp 
        temp3 = head
        while temp.next:
            temp = temp.next
            temp3 = temp3.next
        temp2.val, temp3.val = temp3.val, temp2.val
        return head