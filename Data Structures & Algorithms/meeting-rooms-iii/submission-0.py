import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key=lambda x: x[0])
        meeting_nums = [0] * n

        available = list(range(n))
        busy = []

        for meeting in meetings:
            start,end = meeting[0],meeting[1]

            while busy and busy[0][0] <= start:

                end_time,room = heapq.heappop(busy)
                heapq.heappush(available,room)
            
            if not available:
                duration = end-start
                new_end = duration + busy[0][0]
                end_time,room =heapq.heappop(busy)
                meeting_nums[room] += 1
                heapq.heappush(busy,(new_end,room))
            else:
            
                room = heapq.heappop(available)
                meeting_nums[room] += 1
                heapq.heappush(busy,(end,room))
            
        return meeting_nums.index(max(meeting_nums))



        