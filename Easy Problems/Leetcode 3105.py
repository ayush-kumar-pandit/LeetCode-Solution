class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)
        count = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
                res = max(res,count)
            else:
                count = 1
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                count += 1
                res = max(res,count)
            else:
                count = 1
        return res