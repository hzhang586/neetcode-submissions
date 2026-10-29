class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        ans = nums[0]
        prev1 = nums[0]
        prev2 = nums[0]

        for i in range(1,n):
            cur1 = max(prev1*nums[i],prev2*nums[i],nums[i])
            prev2 = min(prev1*nums[i],prev2*nums[i],nums[i])
            if cur1 > ans:
                ans = cur1
            
            prev1 = cur1
            
        
        return ans