import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m = len(heights)
        n = len(heights[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0

        heap = [(0,0,0)]

        while heap:
            effort,r,c = heapq.heappop(heap)
            if effort > efforts[r][c]:
                continue
            
            if r == m-1 and c == n-1:
                return effort
            
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if not (nr >= 0 and nr < m and nc >= 0 and nc < n):
                    continue
                
                new_effort = max(abs(heights[nr][nc]-heights[r][c]),effort)

                if new_effort < efforts[nr][nc]:
                    efforts[nr][nc] = new_effort
                    heapq.heappush(heap,(new_effort,nr,nc))
        
        return efforts[m-1][n-1]


        