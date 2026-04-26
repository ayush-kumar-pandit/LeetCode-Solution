class Solution:
    def maxFreqSum(self, s: str) -> int:
        d1 = {}
        d2 = {}
        for ch in s:
            if ch in 'aeiou':
                d1[ch] = d1.get(ch, 0) + 1
            else:
                d2[ch] = d2.get(ch, 0) + 1
        res = max(d1.values(), default = 0) + max(d2.values(), default = 0)
        return res