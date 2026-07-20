class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        res = 0
        for i in freq:
            res += freq[i] * (freq[i] - 1) // 2
        
        return res