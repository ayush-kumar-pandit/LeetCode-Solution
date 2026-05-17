class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            x = 0
            while num:
                x = x + num % 10
                num //= 10
            return x
        res = []
        for i in nums:
            res.append(digit_sum(i))
        return min(res)