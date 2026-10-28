class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0],nums[1])
        
        prev2_f = nums[0]
        prev1_f = max(nums[0],nums[1])

        
        for i in range(2,n-1):
            curr_f = max(prev2_f+nums[i],prev1_f)
            
            prev2_f,prev1_f = prev1_f,curr_f
        
       

        prev2_l = nums[1]
        prev1_l = max(nums[1],nums[2])

        for i in range(3,n):
            curr_l = max(prev2_l+nums[i],prev1_l)
            prev2_l,prev1_l = prev1_l,curr_l
        
        
        return max(prev1_f,prev1_l)
        

