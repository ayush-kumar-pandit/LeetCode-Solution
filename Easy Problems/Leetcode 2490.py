class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        prev = words[0][-1]
        for word in words[1:]:
            if prev[-1] != word[0]:
                return False
            prev = word[-1]
        if words[-1][-1] != words[0][0]:
            return False
        return True