class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            res += (i + 1 ) * (ord('z') + 1 - ord(s[i]))
        return res 