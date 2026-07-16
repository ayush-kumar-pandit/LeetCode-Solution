# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1

        num1 = 0
        temp = l1
        while temp:
            num1 = num1 * 10 + temp.val
            temp = temp.next
        
        num2 = 0
        temp = l2
        while temp:
            num2 = num2 * 10 + temp.val
            temp = temp.next
        
        summ = num1 + num2
        if not summ:
            return ListNode(0)
        head = None
        while summ:
            temp = ListNode(summ % 10, head)
            head = temp
            summ //= 10
        return head