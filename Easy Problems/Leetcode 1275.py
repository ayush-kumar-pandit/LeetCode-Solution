class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if 5 > len(moves):
            return 'Pending'
        board = [['','',''],
                 ['','',''],
                 ['','','']]
        turn = 'A'
        for move in moves:
            board[move[0]][move[1]] = turn
            turn = 'B' if turn == 'A' else 'A'
            if (board[0][0] == 'A' and board[1][1] == 'A' and board[2][2] == 'A') or (board[0][2] == 'A' and board[1][1] == 'A' and board[2][0] == 'A') or (board[0][0] == 'A' and board[0][1] == 'A' and board[0][2] == 'A') or (board[1][0] == 'A' and board[1][1] == 'A' and board[1][2] == 'A') or (board[2][0] == 'A' and board[2][1] == 'A' and board[2][2] == 'A') or (board[0][0] == 'A' and board[1][0] == 'A' and board[2][0] == 'A') or (board[0][1] == 'A' and board[1][1] == 'A' and board[2][1] == 'A') or (board[0][2] == 'A' and board[1][2] == 'A' and board[2][2] == 'A'):
                return 'A'

            elif (board[0][0] == 'B' and board[1][1] == 'B' and board[2][2] == 'B') or (board[0][2] == 'B' and board[1][1] == 'B' and board[2][0] == 'B') or (board[0][0] == 'B' and board[0][1] == 'B' and board[0][2] == 'B') or (board[1][0] == 'B' and board[1][1] == 'B' and board[1][2] == 'B') or (board[2][0] == 'B' and board[2][1] == 'B' and board[2][2] == 'B') or (board[0][0] == 'B' and board[1][0] == 'B' and board[2][0] == 'B') or (board[0][1] == 'B' and board[1][1] == 'B' and board[2][1] == 'B') or (board[0][2] == 'B' and board[1][2] == 'B' and board[2][2] == 'B'):
                return 'B'
        if 9 == len(moves):
            return 'Draw'
        return 'Pending'