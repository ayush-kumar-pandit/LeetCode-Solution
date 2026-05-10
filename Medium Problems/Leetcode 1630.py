class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr: list[int]) -> bool:
            if len(arr) <= 2:
                return True
            arr.sort()
            f_dif = arr[1] - arr[0] 
            for i in range(1, len(arr) - 1):
                dif = arr[i + 1] - arr[i]
                if dif != f_dif:
                    return False
            return True
        res = []
        for i in range(len(l)):
            res.append(check(nums[l[i]:r[i] + 1]))
        return res