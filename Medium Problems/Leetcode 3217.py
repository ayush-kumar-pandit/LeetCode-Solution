# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        s1 = set()
        
        for i in nums:
            s1.add(i)
        
        while head and head.val in s1:
            head = head.next
        
        if not head or not head.next:
            return head
        
        cur = head.next
        prev = head
        
        while cur:
            if cur.val in s1:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        
        return head
