class Solution:
    def solveNQueens(self, n: int):
        res = []
        def isValid(board, row ,col):
            duprow, dupcol = row, col
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            
            row, col = duprow, dupcol
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col-=1

            row, col = duprow, dupcol
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1

            return True

        def recurse(col, board):
            if col == n:
                temp = []
                for row in board:
                    temp.append(''.join(row))
                res.append(temp)
                return

            for row in range(n):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    recurse(col+1, board)
                    board[row][col] = '.'
        
        board = [['.' for _ in range(n)]for _ in range(n)]
        recurse(0, board)
        return res

s = Solution()
print(s.solveNQueens(4))