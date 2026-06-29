class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for ch in patterns:
            if ch in word:
                res += 1
        return res