class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = {}
        while n:
            x = n % 10
            freq[x] = freq.get(x, 0) + 1
            n //= 10
        res = 0
        mn = float('inf')
        for k, v in sorted(freq.items()):
            if mn > v:
                mn = v
                res = k
        return res