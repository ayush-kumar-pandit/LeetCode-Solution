class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) != m + 1:
            return False
        arr = []
        for i in range(1, m + 1):
            arr.append(i)
        arr.append(m)

        nums.sort()
        return arr == nums