class Solution:
    def sumAndMultiply(self, n: int) -> int:
        st = str(n)
        conc = 0
        summ = 0
        for i in st:
            if i != '0':
                summ += ord(i) - ord('0')
                conc = conc * 10 + ord(i) - ord('0')
        return conc * summ