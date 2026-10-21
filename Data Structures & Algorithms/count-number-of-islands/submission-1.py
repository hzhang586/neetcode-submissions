class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = 0

        def isValid(row,col):
            return row >= 0 and row < m and col >= 0 and col < n
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == '1':
                    ans += 1
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        (r,c) = queue.popleft()
                        if isValid(r-1,c) and (r-1,c) not in visited and grid[r-1][c] == '1':
                            queue.append((r-1,c))
                            visited.add((r-1,c))
                        if isValid(r+1,c) and (r+1,c) not in visited and grid[r+1][c] == '1':
                            queue.append((r+1,c))
                            visited.add((r+1,c))
                        if isValid(r,c-1) and (r,c-1) not in visited and grid[r][c-1] == '1':
                            queue.append((r,c-1))
                            visited.add((r,c-1))
                        if isValid(r,c+1) and (r,c+1) not in visited and grid[r][c+1] == '1':
                            queue.append((r,c+1))
                            visited.add((r,c+1))


        return ans                
                        
                        
        