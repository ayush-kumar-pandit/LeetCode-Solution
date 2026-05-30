class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        i = 0
        j = n
        left = [0]
        right = [0]
        while i < n and j > 0:
            left.append(left[-1] + nums[i])
            right.append(right[-1] + nums[j])
            i += 1
            j -= 1
        right.reverse()
        res = []
        for i in range(n + 1):
            res.append(abs(left[i] - right[i]))
        return res