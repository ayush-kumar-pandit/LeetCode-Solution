class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = {}
        for arr in nums:
            for x in arr:
                freq[x] = freq.get(x, 0) + 1

        ans = []
        n = len(nums)

        for k, v in freq.items():
            if v == n:
                ans.append(k)

        return sorted(ans)