class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s = set()
        for i in friends:
            s.add(i)

        ls = []
        for i in order:
            if i in s:
                ls.append(i)
        return ls