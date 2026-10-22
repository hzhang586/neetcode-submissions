class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxA = 0
        m = len(grid)
        n = len(grid[0])

        def isValid(r,c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def dfs(i,j):

            if isValid(i,j) and grid[i][j] == 1:
                grid[i][j] = 0
                up = dfs(i-1,j) if isValid(i-1,j) else 0
                down = dfs(i+1,j) if isValid(i+1,j) else 0
                left = dfs(i,j-1) if isValid(i,j-1) else 0
                right = dfs(i,j+1) if isValid(i,j+1) else 0

                return 1 + up + down + left+ right
            return 0
        

        for i in range(m):
            for j in range(n):
                A = dfs(i,j)
                if A > maxA:
                    maxA = A
        return maxA