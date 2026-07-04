class Solution:
    def stringHash(self, s: str, k: int) -> str:
        i_a = {i: chr(ord('a') + i) for i in range(26)}
        n = len(s)
        res = ""
        for i in range(0, n, k):
            j = i
            x = 0
            while j < i + k:
                x += ord(s[j]) - ord('a')
                j += 1
            res += i_a[x % 26]
        return res
            