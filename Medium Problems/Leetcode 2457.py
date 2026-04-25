class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(num: int) -> int:
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            return temp
        if n <= target or digit_sum(n) <= target:
            return 0
        res = 0
        depth = 1
        while True:
            x = n % (10 ** depth)
            res = (10 ** depth) - x
            if digit_sum(n + res) <= target:
                return res
            depth += 1 
            