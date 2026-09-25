class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            x *= -1
            flag += 1 
        n = 0

        while x:
            n = n * 10 + x % 10
            x //= 10
        if n > 2 ** 31 - 1 or n < -2 ** 31:
            return 0
        if flag:
            return n * -1
        return n