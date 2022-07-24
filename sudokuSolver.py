class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(c, row, col, board):
            for i in range(9):
                if board[row][i] == c:
                    return False
                
                if board[i][col] == c:
                    return False
                
                if board[3 * int(row/3) + int(i/3)][3 * int(col/3) + i % 3] == c:
                    return False
                
            return True

        def recurse(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            if isValid(str(c), i, j, board):
                                board[i][j] = str(c)
                                if recurse(board) == True:
                                    return True
                                else:
                                    board[i][j] = '.'

                        return False
            return True

        recurse(board)

s = Solution()
print(s.solveSudoku([
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]))