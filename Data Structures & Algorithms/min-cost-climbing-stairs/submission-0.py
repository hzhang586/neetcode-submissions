class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        i = 0
        j = 0
        n = len(cost)
        min_cost = 0
        for k in range(2,n+1):

            min_cost = min(i+cost[k-2],j+cost[k-1])
            tmp = j
            j = min_cost
            i = tmp
        
        return min_cost



            
        