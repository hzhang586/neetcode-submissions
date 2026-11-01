class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for i,x in enumerate(nums):
            if farthest < i:
                return False
            farthest = max(farthest,x+i)
            
        
        return True