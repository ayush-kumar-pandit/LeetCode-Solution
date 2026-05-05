class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        s = set(allowed)
        for word in words:
            flag = True
            for w in word:
                if w not in s:
                    flag = False
            if flag:
                res += 1 
             
        return res