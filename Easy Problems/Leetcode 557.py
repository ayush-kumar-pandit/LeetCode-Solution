class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for w in s.split():
            res = res + w[::-1] + " "
        return res[:-1] 