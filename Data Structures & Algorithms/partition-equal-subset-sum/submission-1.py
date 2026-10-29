class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2:
            return False
        
        target = numSum // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for x in range(target,num-1,-1):
                dp[x] = dp[x] or dp[x-num]

        return dp[target]        