class Solution:
    def jump(self, nums: List[int]) -> int:

        # numJump = [0 for _ in range(len(nums))]

        # cur = 0
        # for i,x in enumerate(nums):
        #     if x+i > cur:
        #         for j in range(cur+1,min(x+i+1,len(nums))):
        #             if numJump[j] == 0:
        #                 numJump[j] = numJump[i]+1
                
        #         cur = x+i
        
        # return numJump[-1]

        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])

            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        
        return jumps
        