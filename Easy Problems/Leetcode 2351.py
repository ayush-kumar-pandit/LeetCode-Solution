class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = ""
        for ch in s:
            if ch not in st:
                st += ch 
            else:
                return ch