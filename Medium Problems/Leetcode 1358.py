class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        freq = {'a': 0,
                'b': 0,
                'c': 0}
        i = 0
        j = 0
        while j < n:
            freq[s[j]] += 1

            while freq['a'] and freq['b'] and freq['c']:
                res += n - j
                freq[s[i]] -= 1
                i += 1
            j += 1
        return res