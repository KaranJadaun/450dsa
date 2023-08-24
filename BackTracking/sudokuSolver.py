class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if (board[i][j] == "."):
                        for k in range(1, 10):
                            char = str(k)
                            if (isSafe(i, j, board, char) == True):
                                board[i][j] = char
                                if (solve(board) == True):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        def isSafe(i, j, board, char):
            for k in range(9):
                if (board[k][j] == char): 
                    return False
                if (board[i][k] == char):
                    return False
                if (board[3 * (i//3) + k//3][3 * (j //3) + k % 3] == char):
                    return False
            return True
        
        solve(board)
