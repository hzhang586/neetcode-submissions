class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        max_amt_prev = nums[1]
        prefix_max = nums[0]
        max_amt = 0
        for i in range(2,n):
            max_amt = max(max_amt_prev,prefix_max+nums[i])
            prefix_max = max(prefix_max,max_amt_prev)
            max_amt_prev = max_amt
        
        return max_amt
            
        