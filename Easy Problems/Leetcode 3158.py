class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        res = 0
        for i in list(freq.keys()):
            if freq[i] == 2:
                res ^= i
        return res