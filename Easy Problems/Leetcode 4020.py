class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        res = 0
        cur = 0
        for i in requests:
            res += max(cur, i) - min(cur, i)
            cur = i
        return res