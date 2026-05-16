class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) < 3:
            return [-1,-1]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        ls = sorted(list(freq))
        res = []
        for i in ls:
            if not res:
                res.append(i)
            if freq[res[-1]] != freq[i]:
                res.append(i)
                return res     
        return [-1,-1]      