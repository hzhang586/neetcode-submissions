import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            dist_sq = points[i][0]**2 + points[i][1]**2
            if len(heap) < k:
                heapq.heappush(heap,(-dist_sq,i))
            else:
                if -dist_sq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist_sq,i))
        
        ans = [0]*k
        for i in range(k):
            tup = heapq.heappop(heap)
            ans[i] = points[tup[1]]
        
        return ans