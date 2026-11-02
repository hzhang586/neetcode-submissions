class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff = [gas[i]-cost[i] for i in range(len(gas))]
        n =len(diff)
        diff = diff*2
        total = 0
        i=0
        for j in range(len(diff)):
            if j-i == n:
                return i
            total += diff[j]
            while total < 0:
                total -= diff[i]
                i += 1
                
        
        return -1