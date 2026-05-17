class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        cur = 0
        prev = -1
        st = s.split()
        for ch in st:
            if ch.isdigit():
                cur = int(ch)
                if cur <= prev:
                    return False
                prev = cur
        return True