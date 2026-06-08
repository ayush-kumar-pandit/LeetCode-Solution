# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        ls = []
        tail = head
        temp = []
        while tail:
            temp.append(tail.val)
            tail = tail.next
            if not len(temp) % k:
                ls += temp[::-1]
                temp = []
        ls += temp
        tail = head
        for i in ls:
            tail.val = i
            tail = tail.next
        return head

        
