class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        res = []
        for i in nums:
            if i - 1 not in freq and i + 1 not in freq and freq[i] == 1:
                res.append(i)
        return res