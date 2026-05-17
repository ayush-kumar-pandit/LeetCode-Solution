class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ""

        for ch in s:
            st += str(ord(ch) - ord('a') + 1)

        for _ in range(k):
            total = 0
            for digit in st:
                total += int(digit)
            st = str(total)

        return int(st)