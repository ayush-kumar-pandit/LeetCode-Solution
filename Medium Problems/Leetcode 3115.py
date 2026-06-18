class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(x: int) -> bool:
            if x < 2:
                return False

            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            
            return True
                    
        first = second = None

        for i in range(len(nums)):
            if first is None and isPrime(nums[i]):
                first = i
            if isPrime(nums[i]):
                second = i
        return second - first
