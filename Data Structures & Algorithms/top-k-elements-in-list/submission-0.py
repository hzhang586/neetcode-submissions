from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        num_Count = Counter(nums)

        heap = []

        for num,count in num_Count.items():

            heap.append((-count,num))
        
        heapq.heapify(heap)
        
        ans = []
        for _ in range(k):

            freq, num = heapq.heappop(heap)
            ans.append(num)
        
        return ans

        