class Solution:
    def minMoves2(self , nums: list[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        res = 0
        for i in nums:
            res += abs(med - i)

        return res