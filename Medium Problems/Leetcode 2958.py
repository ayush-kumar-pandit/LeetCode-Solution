class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = l = 0
        fq = defaultdict(int)

        for r, ch in enumerate(nums):
            fq[ch] += 1
            while fq[ch] > k:
                fq[nums[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res