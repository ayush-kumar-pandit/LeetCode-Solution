class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = mx = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            mx = max(mx,cur)
        return mx