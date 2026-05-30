class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        s = 0
        for i in range(len(nums) - 1):
            s += nums[i]
            if s >= total - s:
               count += 1 
        return count
