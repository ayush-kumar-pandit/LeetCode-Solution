class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        size = len(arr)
        if k > size:
            return ""
        freq = {}
        for ch in arr:
            freq[ch] = freq.get(ch, 0) + 1
        count = 0
        for ch in list(freq):
            if freq[ch] == 1:
                count += 1
                if count == k:
                    return ch
        return ""