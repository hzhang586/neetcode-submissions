class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
        
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if nr >= 0 and nr < m and nc >=0 and nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c]+1
                    queue.append((nr,nc))




        
        


            

            
            


        