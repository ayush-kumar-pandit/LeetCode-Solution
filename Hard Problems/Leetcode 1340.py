class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1]*n

        for val, i in sorted((val, i) for i, val in enumerate(arr)):
            for j in range(i-1, max(i-d-1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i+1, min(i+d+1, n)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)