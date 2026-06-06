class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        res = 1
        for i in range(1, k + 1):
            res = res * (n - 1 + i) // i
        return res % (10**9 + 7)