class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        res = 0
        for i in freq:
            x = k - i
            if x in freq:
                if i == x:
                    res += freq[i] // 2
                    freq[i] = 0
                else:
                    pairs = min(freq[i], freq[x])
                    res += pairs
                    freq[i] -= pairs
                    freq[x] -= pairs
        return res