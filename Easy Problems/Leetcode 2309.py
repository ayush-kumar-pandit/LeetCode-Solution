class Solution:
    def greatestLetter(self, s: str) -> str:
        s1 = set(s)
        for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if ch.lower() in s1 and ch in s1:
                return ch
        return ""