class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1],reverse = True)
        res = 0
        for actual, minimum in tasks:
            res = max(minimum,res + actual)
        return res