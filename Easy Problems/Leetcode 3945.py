class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}
        while n:
            i = n % 10
            freq[i] = freq.get(i, 0) + 1
            n //= 10
        res = 0
        for i in freq:
            res += i * freq[i]
        return res