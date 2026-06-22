class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(s) < len(target):
            return 0
        freq = {}
        for ch in s:
            if ch in target:
                freq[ch] = freq.get(ch, 0) + 1
        if not freq:
            return 0
        for ch in target:
            if ch not in freq:
                return 0
        res = []
        for key, val in freq.items():
            res.append(val // target.count(key))
        return min(res)