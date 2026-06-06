class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        for i in nums:
            if i < 10:
                single += i
        return not single == sum(nums) / 2