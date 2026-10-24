from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timestamps_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.timestamps_dict[key].append((timestamp,value))



        

    def get(self, key: str, timestamp: int) -> str:
        
        timestamps = self.timestamps_dict[key]
        left = -1
        right = len(timestamps)
        while left+1 < right:
            mid = (left+right) // 2

            if timestamps[mid][0] <= timestamp:
                left = mid
            else:
                right = mid
        
        if right == 0:
            return ""
        return timestamps[left][1]
        
