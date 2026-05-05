class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        s = a
        while len(a) < len(b):
            res += 1
            a += s
        if b in a:
            return res
        res += 1
        a += s
        if b in a:
            return res
        return -1