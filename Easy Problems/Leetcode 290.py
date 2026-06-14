class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_str = s.split()
        if len(pattern) != len(new_str):
            return False
        rel = {}
        for i in range(len(pattern)):
            if pattern[i] not in rel:
                if new_str[i] in rel.values():
                    return False
                rel[pattern[i]] = new_str[i]
            else:
                if rel[pattern[i]] != new_str[i]:
                    return False
        return True