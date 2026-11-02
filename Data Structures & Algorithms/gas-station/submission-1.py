class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff = [gas[i]-cost[i] for i in range(len(gas))]
        n =len(diff)
        total = 0
        i=0
        for j in range(2*n):
            if j != i and (j-i) % n == 0:
                return i
            total += diff[j%n]
            while total < 0:
                total -= diff[i%n]
                i += 1
            
                
        
        return -1