class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m = len(board)
        n = len(board[0])
        switch = [[True] * n for _ in range(m)]

        directions = [[1,0],[-1,0],[0,1],[0,-1]]


        def dfs(r,c):
         
            if board[r][c] == 'X':
                return

            switch[r][c] = False

            for dr,dc in directions:
                nr,nc  = r+dr,c+dc

                if (nr >= 0 and
                    nr < m and
                    nc >= 0 and
                    nc < n and switch[nr][nc] == True):

                    dfs(nr,nc)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and switch[i][j]:
                    board[i][j] = 'X'
