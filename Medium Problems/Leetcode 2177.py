class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        if x * 3 != num:
            return []
        return [x-1,x,x+1]
         