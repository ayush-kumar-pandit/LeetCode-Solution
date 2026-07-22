class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def IsWhite(cords: str) -> bool:
            x = ord(cords[0]) - ord('a') + 1
            y = int(cords[1])

            if x % 2 and y % 2:
                return False
            elif y % 2 and x % 2 == 0:
                return True
            elif x % 2 and y % 2 == 0:
                return True
            else:
                return False
        
        return IsWhite(coordinate1) == IsWhite(coordinate2)