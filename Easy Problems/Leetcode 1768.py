class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        m = len(word1)
        n = len(word2)

        while i < m and i < n:
            res += word1[i] + word2[i]
            i += 1
        if m == n:
            return res
        elif i == m:
            while i < n:
                res += word2[i]
                i += 1
        else:
            while i < m:
                res += word1[i]
                i += 1
        return res