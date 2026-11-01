class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        del_count = 0
        n = len(intervals)
        intervals.sort(key=lambda x:x[1])
        cur = intervals[0]

        for i in range(1,n):
            if intervals[i][0] >= cur[1]:
                cur = intervals[i]
            else:
                del_count += 1
        
        return del_count
        