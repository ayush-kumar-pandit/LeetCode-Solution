class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        mn=min(nums)

        ans=mx-mn - 2 *k

        return max(0,ans)
        