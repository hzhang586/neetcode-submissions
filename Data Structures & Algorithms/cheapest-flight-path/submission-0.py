class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dist = [[float('inf')]*(k+2) for _ in range(n)]

        dist[src][0] = 0

        for j in range(k+1):
            for u,v, price in flights:
                if dist[u][j] != float('inf'):
                    dist[v][j+1] = min(dist[v][j+1],dist[u][j]+price)
        
        ans = min(dist[dst])

        return -1 if ans == float('inf') else ans
        