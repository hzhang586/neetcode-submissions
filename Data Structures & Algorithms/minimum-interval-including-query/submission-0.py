import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key = lambda x:x[0])
        pairs = [(x,i) for i,x in enumerate(queries)]
        pairs.sort(key = lambda x:x[0])
        
        ans = [-1 for _ in range(len(queries))]

        heap = []
        i = 0
        for pair in pairs:
            q = pair[0]
            while i < len(intervals) and intervals[i][0] <= q:
                left = intervals[i][0]
                right = intervals[i][1]
                heapq.heappush(heap,(right-left+1,right))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                ans[pair[1]] = heap[0][0]
        
        return ans
                
        