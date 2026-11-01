class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        ans = [intervals[0]]
        
        for i in range(1,n):
            cur = intervals[i]
            prev = ans[-1]
            if not (prev[1] >= cur[0] and cur[1] >= prev[0]):
                ans.append(cur)
            else:
                ans[-1] = [min(prev[0],cur[0]),max(prev[1],cur[1])]
        
        return ans


        