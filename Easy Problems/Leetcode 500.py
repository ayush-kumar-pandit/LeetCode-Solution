class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiopQWERTYUIOP")
        r2 = set("asdfghjklASDFGHJKL")
        r3 = set("zxcvbnmZXCVBNM")
        row = {}
        for ch in r1:
            row[ch] = 1
        for ch in r2:
            row[ch] = 2
        for ch in r3:
            row[ch] = 3

        res = []
        for word in words:
            x = row[word[0]]
            n = len(word)
            count = 0
            for ch in word:
                if row[ch] != x:
                    break
                count += 1
            if count == n:
                res.append(word)
        return res