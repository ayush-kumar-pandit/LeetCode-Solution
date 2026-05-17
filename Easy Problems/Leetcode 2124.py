class Solution:
    def checkString(self, s: str) -> bool:
        prev = ""
        for ch in s:
            if ch == 'a':
                if prev == 'b':
                    return False
            prev = ch
        return True