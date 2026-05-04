from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        global_max = nums[0]
        idx = 0
        for i in range(1, len(nums)):
            global_max = max(global_max, nums[i])

            if nums[i] < left_max:
                idx = i
                left_max = global_max

        return idx + 1