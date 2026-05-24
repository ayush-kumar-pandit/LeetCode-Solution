class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] <= k:
                res.append(i)
        return res