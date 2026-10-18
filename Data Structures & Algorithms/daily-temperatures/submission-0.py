class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0 for _ in range(len(temperatures))]
        stack  = []

        for i,x in enumerate(temperatures):

            while stack and x > stack[-1][0]:
                tup = stack.pop()
                ans[tup[1]] = i - tup[1]
            
            stack.append((x,i))
        
        return ans

        