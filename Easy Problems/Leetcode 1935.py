class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                res += 1
        return res