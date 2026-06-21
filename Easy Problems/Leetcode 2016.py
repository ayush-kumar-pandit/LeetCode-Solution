class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = [0] * (n + 1)
        maxx = nums[-1]
        for i in range(n, -1, -1):
            if maxx < nums[i]:
                maxx = nums[i]
            res[i] = maxx - nums[i]
        
        if not max(res):
            return -1
        return max(res)