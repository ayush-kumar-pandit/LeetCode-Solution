class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if not maxDoubles:
            return target - 1
        
        step = 0
        
        while maxDoubles and target > 1:
            if target & 1:
                target -= 1
                step += 1
            else:
                target //= 2
                step += 1
                maxDoubles -= 1
        if not target:
            return step
        return step + target - 1