class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for c in s:
            dist = (26 - (ord(c) - ord('a'))) % 26
            ans = max(ans, dist)
        return ans

