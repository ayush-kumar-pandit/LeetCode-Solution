class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a') + 1
        y = int(coordinates[1])

        if x % 2 and y % 2:
            return False
        elif y % 2 and x % 2 == 0:
            return True
        elif x % 2 and y % 2 == 0:
            return True
        else:
            return False