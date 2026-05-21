class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur = sum(i * nums[i] for i in range(n))
        ans = cur
        for k in range(1, n):
            cur = cur + total - n * nums[n - k]
            ans = max(ans, cur)

        return ans