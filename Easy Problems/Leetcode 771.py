class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        res = 0
        for st in stones:
            if st in s:
                res += 1
        return res