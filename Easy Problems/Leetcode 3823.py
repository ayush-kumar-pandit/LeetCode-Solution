class Solution:
    def reverseByType(self, s: str) -> str:
        alpha = ""
        symbol = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                alpha += s[i]
            else:
                symbol += s[i]
        al = 0
        sy = 0
        res = ""
        for i in range(len(s)):
            if s[i].isalpha():
                res += alpha[al]
                al += 1
            else:
                res += symbol[sy]
                sy += 1
        return res