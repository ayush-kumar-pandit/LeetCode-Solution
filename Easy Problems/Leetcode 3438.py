class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        res = ""
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if freq[s[i]] == int(s[i]) and freq[s[i + 1]] == int(s[i + 1]):
                    res = s[i] + s[i + 1]
                    break
        return res