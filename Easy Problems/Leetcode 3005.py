class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        mx = max(freq.values())
        res = 0
        for i in freq:
            if freq[i] == mx:
                res += mx 
        return res