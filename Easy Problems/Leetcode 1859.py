class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)
        for word in words:
            idx = int(word[-1]) - 1
            res[idx] = word[:-1]
        return " ".join(res)