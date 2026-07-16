"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        st = []
        tail = head
        while tail or st:
            if tail.child:
                if tail.next:
                    st.append(tail.next)
                tail.next = tail.child
                tail.child.prev = tail
                tail.child = None
            if tail.next is None and st:
                tail.next = st.pop()
                tail.next.prev = tail
            tail = tail.next
        return head
        