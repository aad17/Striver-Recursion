class Solution:
    def solveNQueens(self, n: int):
        ans = []
        def recurse(col, board, leftrow, lowerdiagonal, upperdiagonal):
            if col == n:
                ans.append(board.copy())
                return

            for row in range(n):
                if leftrow[row] == 0 and lowerdiagonal[row+col] == 0 and upperdiagonal[n-1+col-row] == 0:
                    board[row][col] = 'Q'
                    leftrow[row] = 1
                    lowerdiagonal[row+col] = 1
                    upperdiagonal[n-1+col-row] = 1
                    recurse(col+1, board, leftrow, lowerdiagonal, upperdiagonal)
                    board[row][col] = '.'
                    leftrow[row] = 0
                    lowerdiagonal[row+col] = 0
                    upperdiagonal[n-1+col-row] = 0
        
        board = [['.' for _ in range(n)]for _ in range(n)]
        leftrow = [0] * n
        lowerdiagonal = [0] * (2*n - 1)
        upperdiagonal = [0] * (2*n - 1)
        recurse(0, board, leftrow, lowerdiagonal, upperdiagonal)
        return ans

s = Solution()
print(s.solveNQueens(4))