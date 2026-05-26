class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}
        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch] = i
            else:
                c = ch.lower()
                if c not in upper:
                    upper[c] = i
        res = 0
        for ch in lower:
            if ch in upper and lower[ch] < upper[ch]:
                res += 1
        return res