# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        temp = head
        while temp != None:
            if temp.val not in freq:
                freq[temp.val] = 1
            else:
                freq[temp.val] += 1
            temp = temp.next
        res = ListNode()
        temp = res
        for i in freq:
            if freq[i] == 1:
                temp.next = ListNode()
                temp = temp.next
                temp.val = i
        return res.next
