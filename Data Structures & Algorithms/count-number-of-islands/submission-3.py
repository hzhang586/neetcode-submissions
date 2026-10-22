class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = 0

        def isValid(row,col):
            return row >= 0 and row < m and col >= 0 and col < n

        def dfs(r,c):
            if not isValid(r,c):
                return
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        

        for i in range(m):
            for j in range(n):
                if  grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
        return ans                
                        
                        
        