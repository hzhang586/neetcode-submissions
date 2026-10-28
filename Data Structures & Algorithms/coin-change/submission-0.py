class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        
        min_deno = min(coins)
        
        dp = []
        dp.append(0)
        for _ in range(1,min_deno):
            dp.append(float('inf'))
        
        
        for amt in range(min_deno,amount+1):

            min_coins = float('inf')

            for coin in coins:
                print(amt-coin)
                if amt - coin >= 0 and dp[amt-coin]+1 < min_coins:
                    min_coins = dp[amt-coin]+1
            dp.append(min_coins)
        

        return dp[-1] if dp[-1] != float('inf') else -1