class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        arr = sorted(c.keys(), key=lambda x: (-c[x], x))
        return arr[:k]