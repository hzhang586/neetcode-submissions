class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp = [[1]* n for _ in range(m)]

        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]

        dp = [1] * n 

        for i in range(1,m):
            dp1 = [1]*n
            for j in range(1,n):
                dp1[j] = dp[j]+dp1[j-1]
            
            dp = dp1
        
        return dp[-1]