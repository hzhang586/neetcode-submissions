"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        schedules = []
        for interval in intervals:
            schedules.append([interval.start,interval.end])
        
        schedules.sort(key=lambda x: x[0])
        cur = schedules[0]
        for i in range(1,len(intervals)):
            if schedules[i][0] < cur[1]:
                return False
            
            cur = schedules[i]
        
        return True

        
