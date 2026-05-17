class Solution:
    def check(self, nums: List[int]) -> bool:
        doubled_nums = nums[:] + nums[:]
        nums.sort()
        for i in range(len(nums)):
            if doubled_nums[i:i+len(nums)] == nums:
                return True
        return False