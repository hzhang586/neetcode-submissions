import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        minTime = dict()
        for i in range(1,n+1):
            if i == k:
                minTime[i] = 0
            else:
                minTime[i] = float('inf')
        
        graph = defaultdict(list)

        for time in times:
            u = time[0]
            v = time[1]
            t = time[2]
            graph[u].append((t,v))
        heap =[(0,k)]
        while heap:
            t,u = heapq.heappop(heap)
            if t > minTime[u]:
                continue
            for time,v in graph[u]:
                if time+t < minTime[v]:
                    minTime[v] = min(minTime[v],time+t)
                    heapq.heappush(heap,(minTime[v],v))
                
           
        ans = 0
        for i in range(1,n+1):
            if minTime[i] == float('inf'):
                return -1
            ans = max(ans,minTime[i])
        
        return ans
        

        