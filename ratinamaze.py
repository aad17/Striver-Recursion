class Solution:
    def findPath(self, m, n):
        visited = [[0 for _ in range(n)]for _ in range(n)]
        ans = []
        visited[0][0] = 1

        def recurse(i, j, s):
            if i == n-1 and j == n-1:
                ans.append(s[:])
                return
 
            # Down          
            if i+1 < n:
                if m[i+1][j] == 1 and visited[i+1][j] != 1:
                    visited[i+1][j] = 1
                    recurse(i+1, j, s+'D')
                    visited[i+1][j] = 0
            
            # Left
            if j-1 >= 0:
                if m[i][j-1] == 1 and visited[i][j-1] != 1:
                    visited[i][j-1] = 1
                    recurse(i, j-1, s+'L')
                    visited[i][j-1] = 0
            
            # Right
            if j+1 < n:
                if m[i][j+1] == 1 and visited[i][j+1] != 1:
                    visited[i][j+1] = 1
                    recurse(i, j+1, s+'R')
                    visited[i][j+1] = 0

            # Up
            if i-1 >= 0:
                if m[i-1][j] == 1 and visited[i-1][j] != 1:
                    visited[i-1][j] = 1
                    recurse(i-1, j, s+'U')
                    visited[i-1][j] = 0

        recurse(0, 0, '')
        return ans if len(ans) > 0 else -1

s = Solution()
# print(s.findPath([
# [1, 0, 0, 0],
# [1, 1, 0, 1],
# [1, 1, 0, 0],
# [0, 1, 1, 1]
# ], 4))
print(s.findPath([[1, 0], [1, 0]], 2))