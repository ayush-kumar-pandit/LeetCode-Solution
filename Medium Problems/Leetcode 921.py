class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        sz = op = 0
        for ch in s:
            if ch == '(':
                sz += 1
            elif sz > 0:
                sz -= 1
            else:
                op += 1
        return op + sz
