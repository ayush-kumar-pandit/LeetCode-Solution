class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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