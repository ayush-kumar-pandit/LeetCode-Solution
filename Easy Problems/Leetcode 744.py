class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z' or ord(target) < ord(letters[0]) or ord(target) >= ord(letters[-1]):
            return letters[0]
        l = 0
        r = len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2
            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                r = mid
        return letters[l]