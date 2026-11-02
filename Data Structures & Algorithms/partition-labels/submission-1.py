class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        intervals = []
        char_dict = {}
        idx = 0
        for i,c in enumerate(s):
            if c not in char_dict:
                intervals.append([i,i])
                char_dict[c] = idx
                idx += 1
            else:
                intervals[char_dict[c]][1] = i
        
        merge = [intervals[0]]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] < merge[-1][1]:
                merge[-1] = [merge[-1][0],max(interval[1],merge[-1][1])]
            else:
                merge.append(interval)
        
        ans = [0] * len(merge)
        for i in range(len(ans)):
            ans[i] = merge[i][1]-merge[i][0]+1
        
        return ans
        


        