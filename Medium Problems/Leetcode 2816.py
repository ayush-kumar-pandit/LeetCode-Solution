# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        temp = head
        while temp:
            num = num * 10 + temp.val
            temp = temp.next
        if num:
            num *= 2
            ans = None
            while num:
                x = num % 10
                ans = ListNode(x,ans)
                num //= 10
            return ans
        else:
            return head