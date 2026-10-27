class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        i = 1
        j = 1
        dp = 0
        for _ in range(2,n+1):
            dp = i+j
            tmp = j
            j = dp
            i = tmp
        
        return dp
        