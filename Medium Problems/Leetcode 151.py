class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        res = ""
        for i in range(len(ls) - 1, -1, -1):
            res = res + ls[i] + ' '
        res = res.strip()
        return res