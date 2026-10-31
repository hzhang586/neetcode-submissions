class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        last = dict()

        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1,n+1):
            last[j] = 0
        
        for i in range(1,m+1):
            print(i)
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    if not last[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j-1] + dp[last[j]][j]
                    last[j] = i
                    
                else:
                    dp[i][j] = dp[i-1][j]
            print(dp)    
        return dp[m][n]  