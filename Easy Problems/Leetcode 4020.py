class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        res = 0
        cur = 0
        for i in requests:
            res += abs(i - cur)
            cur = i
        return res