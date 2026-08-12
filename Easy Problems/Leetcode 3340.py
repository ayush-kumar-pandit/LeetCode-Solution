class Solution:
    def isBalanced(self, num: str) -> bool:
        x = 0
        y = 0
        n = len(num)
        for i in range(n):
            if i & 1:
                y += ord(num[i]) - ord('0')
            else:
                x += ord(num[i]) - ord('0')
        return x == y