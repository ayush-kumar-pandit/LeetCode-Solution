class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        res = 0
        for i in nums:
            res += i - mn
        return res