class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        x = nums[0]
        y = nums[1]
        z = nums[2]

        if x < y:
            if y < z:
                return y
            else:
                return z if x < z else x
        else:
            if x < z:
                return x
            else:
                return z if y < z else y