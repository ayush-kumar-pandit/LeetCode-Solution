class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        x = 10
        turn = True
        while n >= x:
            n -= x
            x -= 1
            turn = False if turn == True else True
        return True if not turn else False