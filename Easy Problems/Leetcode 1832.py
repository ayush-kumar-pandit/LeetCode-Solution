class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        arr = [0] * 26
        for c in sentence:
            arr[ord(c) - ord('a')] += 1
        for i in arr:
            if not i:
                return False
        return True