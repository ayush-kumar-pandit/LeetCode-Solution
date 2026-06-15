class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squareSum = 0
        digitSum = 0
        while n:
            x = n % 10
            squareSum += x * x
            digitSum += x
            n //= 10
        return squareSum - digitSum >= 50