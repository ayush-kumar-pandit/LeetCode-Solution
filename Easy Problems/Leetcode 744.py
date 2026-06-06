class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z' or ord(target) < ord(letters[0]) or ord(target) >= ord(letters[-1]):
            return letters[0]
        for letter in letters:
            if ord(target) < ord(letter):
                return letter