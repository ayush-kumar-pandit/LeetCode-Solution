class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_div(n):
            temp = n
            while temp:
                x = temp % 10
                if not x:
                    return False
                elif n % x != 0:
                    return False
                temp //= 10
            return True
        res = []
        for i in range(left, right + 1):
            if self_div(i):
                res.append(i)
        return res