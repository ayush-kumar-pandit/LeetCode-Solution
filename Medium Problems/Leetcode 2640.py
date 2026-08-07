class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        mx = 0
        prefix_sum = 0

        for num in nums:
            mx = max(mx, num)
            prefix_sum += num + mx
            ans.append(prefix_sum)

        return ans