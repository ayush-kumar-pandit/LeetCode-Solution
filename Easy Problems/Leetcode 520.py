class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = word.upper()
        lower = word.lower()
        cap = word.capitalize()
        return word == upper or word == lower or word == cap