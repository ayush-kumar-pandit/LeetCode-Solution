class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            else:
                res += len(word)
        return res