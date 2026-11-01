class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # prefixSum =[0] * (len(nums)+1)
        # for i in range(1,len(nums)+1):
        #     prefixSum[i] = prefixSum[i-1]+nums[i-1]
        
        
        # minSums = [0]*len(nums)
        # minSum = 0
        # for i in range(1,len(nums)+1):
        #     if prefixSum[i-1] < minSum:
        #         minSum = prefixSum[i-1]
        #     minSums[i-1] = minSum
        
        # maxSum = float('-inf')

        # for i in range(1,len(nums)+1):
        #     maxSum = max(maxSum,prefixSum[i]-minSums[i-1]) 

        # return maxSum    

        ans = float('-inf')
        prefix = 0
        min_prefix = 0

        for x in nums:
            prefix += x
            ans = max(ans,prefix - min_prefix)
            min_prefix = min(min_prefix,prefix)
        
        return ans
        