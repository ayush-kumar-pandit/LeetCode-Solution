class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        words = ""
        for ch in range(len(s) - 1, -1, -1):
            if s[ch].isalpha():
                words += s[ch]
        j = 0
        res = ""
        for i in range(len(s)):
            if not s[i].isalpha():
                res += s[i]
            else:
                if j >= len(words):
                    break
                res += words[j]
                j += 1
        return res