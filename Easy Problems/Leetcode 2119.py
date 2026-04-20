class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num
        x = 0
        while temp:
            x = x * 10 + temp % 10
            temp //= 10
        temp = x
        y = 0
        while temp:
            y = y * 10 + temp % 10
            temp //= 10
        return y == num 