class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = int(len(nums) * (len(nums) + 1) / 2)
        sum = 0
        for i in nums:
            sum += i
        return x - sum
