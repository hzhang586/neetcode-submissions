class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        maxSum = sum(nums)
        minSum = -maxSum
        maxNum = max(nums)
        if target < minSum or target > maxSum:
            return 0

        dp = [ 0 for _ in range(minSum-maxNum, maxSum+maxNum+1)]
        dp[maxSum+maxNum] = 1
        for num in nums:
            dp1 = [ 0 for _ in range(minSum-maxNum, maxSum+maxNum+1)]
            for x in range(minSum,maxSum+1):
                dp1[maxSum+maxNum+x] =  dp[maxSum+maxNum+x+num] + dp[maxSum+maxNum+x-num]
            dp = dp1
        

        return dp[maxSum+maxNum+target]