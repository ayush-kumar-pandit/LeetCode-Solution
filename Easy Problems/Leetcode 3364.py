class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for L in range(l, r + 1):
            if L > n:
                break
            window = sum(nums[:L])         
            if 0 < window < min_sum:
                min_sum = window
            for i in range(1, n - L + 1):
                window += nums[i + L - 1] - nums[i - 1]  
                if 0 < window < min_sum:
                    min_sum = window

        return min_sum if min_sum != float('inf') else -1