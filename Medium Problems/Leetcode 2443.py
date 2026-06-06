class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num, num // 2 - 1, -1):
            if i + int(str(i)[::-1]) == num:
                return True
        return False