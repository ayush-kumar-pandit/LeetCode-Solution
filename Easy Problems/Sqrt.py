class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low = 0
        high = x
        while high >= low:
            mid = int((high + low)/2)

            if mid * mid == x or mid * mid < x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            
            