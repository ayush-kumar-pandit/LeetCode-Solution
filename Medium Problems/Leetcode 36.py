class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            cols = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in rows:
                        return False
                    rows.add(board[i][j])
                if  board[j][i].isdigit():
                    if board[j][i] in cols:
                        return False
                    cols.add(board[j][i])
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                matrix = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j].isdigit():
                            if board[i][j] in matrix:
                                return False
                            matrix.add(board[i][j])
        return True