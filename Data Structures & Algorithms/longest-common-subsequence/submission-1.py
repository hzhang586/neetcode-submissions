class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1,n):
            if text1[0] == text2[i] or dp[0][i-1]:
                dp[0][i] = 1

        for j in range(1,m):
            if text2[0] == text1[j] or dp[j-1][0]:
                dp[j][0] = 1
        

        for i in range(1,m):
            for j in range(1,n):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        

        return dp[m-1][n-1]
        