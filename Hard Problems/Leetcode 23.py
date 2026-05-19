# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ls = []
        for nodes in lists:
            temp = nodes
            while temp:
                ls.append(temp.val)
                temp = temp.next
        ls.sort()
        head = ListNode()
        tail = head
        for i in ls:
            tail.next = ListNode(i)
            tail = tail.next
        return head.next