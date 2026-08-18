class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        r = l = 0
        n = len(nums) - 1
        while r < n:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            jumps += 1
            r = farthest
        return jumps