class Solution:
    def add_digits(self, x):
        sum = 0
        while(x):
            sum += x % 10
            x //= 10
        return sum
        
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = {}
        while(lowLimit <= highLimit):
            temp = self.add_digits(lowLimit)
            if temp in dic:
                dic[temp] += 1
            else:
                dic[temp] = 1
            lowLimit += 1
        return max(dic.values())
        