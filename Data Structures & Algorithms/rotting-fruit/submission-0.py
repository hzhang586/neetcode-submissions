import math
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(row,col):
            return  row >=0 and row < len(grid) and col >=0 and col < len(grid[0])
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        min_min = 0
        minutes = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    minutes[i][j] = -1
                elif grid[i][j] == 1:
                    minutes[i][j] = float('inf')
                else:
                    queue.append([i,j])
        while queue:
            [r,c] = queue.popleft()
            if isValid(r-1,c):
                if math.isinf(minutes[r-1][c]):
                    minutes[r-1][c] = minutes[r][c]+1

                    queue.append([r-1,c])
            
            if isValid(r+1,c):
                if math.isinf(minutes[r+1][c]):
                    minutes[r+1][c] = minutes[r][c]+1
                    queue.append([r+1,c])
            
            if isValid(r,c-1):
                if math.isinf(minutes[r][c-1]):
                    minutes[r][c-1] = minutes[r][c]+1
                    queue.append([r,c-1])

            if isValid(r,c+1):
                if math.isinf(minutes[r][c+1]):
                    minutes[r][c+1] = minutes[r][c]+1
                    queue.append([r,c+1])
        for i in range(m):
            for j in range(n):
                if math.isinf(minutes[i][j]):
                    return -1
                min_min = max(min_min, minutes[i][j])
        
        return min_min

