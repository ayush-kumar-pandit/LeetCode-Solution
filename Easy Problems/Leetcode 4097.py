class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        res = inf
        for i in range(0,len(nums) - 1, 2):
            temp = nums[i]
            x = len(str(nums[i + 1]))
            while x:
                temp *= 10
                x -= 1
            temp += nums[i + 1]
            res = min(res,temp)
        return res