import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        dist_sq_l = [0]*n
        for i,cor in enumerate(points):
            dist_sq_l[i] = cor[0]**2 + cor[1]**2
        
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            if len(heap) < k:
                heapq.heappush(heap,(-dist_sq_l[i],i))
            else:
                if -dist_sq_l[i] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist_sq_l[i],i))
        
        ans = [0]*k
        for i in range(k):
            tup = heapq.heappop(heap)
            ans[i] = points[tup[1]]
        
        return ans