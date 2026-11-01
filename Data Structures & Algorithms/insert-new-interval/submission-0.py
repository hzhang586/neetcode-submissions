class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                ans.append(interval)
                i += 1
                continue
            if interval[1] >= newInterval[0] and newInterval[1] >= interval[0]:
                newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
                i += 1
            else:
                break
        
        ans.append(newInterval)
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        
        return ans
        
            
        