class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        memo = [[0]* n for _ in range(m)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        ans = 0

        def dfs(r,c):

            if memo[r][c] != 0:
                return memo[r][c]

            best = 1

            for dr,dc in directions:
                nr, nc = dr+r,dc+c
                if nr >= 0 and nr < m and nc >= 0 and nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best,1+dfs(nr,nc))
            
            memo[r][c] = best

            return best

        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
        
        return ans
        

        