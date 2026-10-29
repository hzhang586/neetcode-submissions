class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        
        min_deno = min(coins)
        
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for amt in range(1,amount+1):

            min_coins = dp[amt]

            for coin in coins:
                if amt - coin >= 0 and dp[amt-coin]+1 < min_coins:
                    min_coins = dp[amt-coin]+1
            dp[amt] = min_coins
        

        return dp[-1] if dp[-1] != float('inf') else -1