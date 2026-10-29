class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)

        # if n == 1:
        #     return 1
        
        # dp = [1]* n
        # ans = 1
        # for i in range(1,n):
        #     max_sub = 1
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if dp[j] + 1 > max_sub:
        #                 max_sub = dp[j]+1
        #                 if max_sub > ans:
        #                     ans = max_sub
            
        #     dp[i] = max_sub
        # return ans

        n = len(nums)
        if n == 1:
            return 1
        
        tails = [nums[0]]
        for i in range(1,n):
            x = nums[i]
            left,right = -1,len(tails)
            while left+1 < right:
                mid = (left+right) // 2
                if tails[mid] < x:
                    left = mid
                else:
                    right = mid
            
            if right == len(tails):
                tails.append(x)
            else:
                tails[right] = x
        
        return len(tails)

        