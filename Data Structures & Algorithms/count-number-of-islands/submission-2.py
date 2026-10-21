class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = 0

        def isValid(row,col):
            return row >= 0 and row < m and col >= 0 and col < n
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if  grid[i][j] == '1':
                    ans += 1
                    queue.append((i,j))
                    grid[i][j] = '0'
                    while queue:
                        (r,c) = queue.popleft()
                        for dr,dc in directions:
                            nr,nc = r+dr,c+dc
                            if isValid(nr,nc) and grid[nr][nc] == '1':
                                queue.append((nr,nc))
                                grid[nr][nc] = '0'

        return ans                
                        
                        
        