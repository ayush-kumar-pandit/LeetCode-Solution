class Solution:
    def maximumCandies(self, candies, k):
        left = 1
        right = sum(candies) // k
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            children = 0
            for c in candies:
                children += c // mid

            if children >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
