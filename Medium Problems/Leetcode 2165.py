class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            ls = []
            num = num * -1
            while num:
                ls.append(num % 10)
                num //= 10
            res = 0
            ls.sort(reverse = True)
            for i in ls:
                res = res * 10 + i
            return -res
        else:
            ls = []
            while num:
                ls.append(num % 10)
                num //= 10
            ls.sort()
            i = 0 
            while i < len(ls) and ls[i] == 0:
                i += 1
            if i >= len(ls):
                return 0 
            res = ls[i]
            zero = i
            while zero:
                res *= 10
                zero -= 1

            i += 1
            while i < len(ls):
                res = res * 10 + ls[i]
                i += 1
            return res