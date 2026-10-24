import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 0
        right = max(piles)+1

        while left+1 < right:
            mid = (left+right) // 2

            if sum([math.ceil(piles[i]/mid) for i in range(len(piles))]) <= h:
                right = mid
            
            else:
                left = mid
        
        return right
        