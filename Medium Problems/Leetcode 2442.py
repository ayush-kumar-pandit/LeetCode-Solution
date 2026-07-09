class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            rev = 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            return rev
        n = len(nums)
        for i in range(n):
            nums.append(reverse(nums[i]))
        return len(set(nums))