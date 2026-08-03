class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        x = len(nums)
        while x > 1:
            for i in range(x - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            x -= 1
        return nums[0]