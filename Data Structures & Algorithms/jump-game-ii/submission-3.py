class Solution:
    def jump(self, nums: List[int]) -> int:

        numJump = [0 for _ in range(len(nums))]

        cur = 0
        for i,x in enumerate(nums):
            if x+i > cur:
                for j in range(cur+1,min(x+i+1,len(nums))):
                    if numJump[j] == 0:
                        numJump[j] = numJump[i]+1
                
                cur = x+i
        
        return numJump[-1]
        