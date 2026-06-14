class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIsomorphic(s: str, t: str) -> bool:
            rel = {}
            for i in range(len(s)):
                if s[i] not in rel:
                    if t[i] in rel.values():
                        return False
                    rel[s[i]] = t[i]
                else:
                    if rel[s[i]] != t[i]:
                        return False
            return True
        res = []
        for word in words:
            if isIsomorphic(pattern,word):
                res.append(word)
        return res