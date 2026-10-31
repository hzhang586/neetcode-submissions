import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        heapq.heapify(heap)
        n = len(nums)
        for i,x in enumerate(nums):
            if i < k:
                heapq.heappush(heap,x)
            else:
                if x > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,x)
        
        return heap[0]