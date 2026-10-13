class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        res = 0
        for i in range(n // 2):
            res -= nums[i]
        for i in range(n // 2, n):
            res += nums[i]
        return res