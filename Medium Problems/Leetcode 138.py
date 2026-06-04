class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newList = {}

        curr = head
        while curr:
            newList[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            newList[curr].next = newList.get(curr.next)
            newList[curr].random = newList.get(curr.random)
            curr = curr.next

        return newList[head]