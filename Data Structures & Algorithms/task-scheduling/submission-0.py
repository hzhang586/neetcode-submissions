import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        t = 0
        task_count = Counter(tasks)
        heap = [-count for count in task_count.values()]
        heapq.heapify(heap)
        
        cooldown = deque()
        while heap or cooldown:
            t += 1
            if cooldown and cooldown[0][1] <= t:
                count, available_time = cooldown.popleft()
                heapq.heappush(heap,count)
            
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count != 0:
                    available_time = t+n+1
                    cooldown.append((count,available_time))
            



        return t


        