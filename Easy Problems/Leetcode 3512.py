class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm = sum(nums)
        count = 0
        while sm % k:
            sm -= 1
            count += 1
        return count