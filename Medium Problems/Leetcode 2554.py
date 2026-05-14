class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        s = set(banned)
        acc = 0
        for i in range(1, n + 1):
            if i not in s:
                if acc + i <= maxSum:
                    acc += i 
                    res += 1
        return res