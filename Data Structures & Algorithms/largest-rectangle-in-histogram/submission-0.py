class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0 

        stack = []

        for i,x in enumerate(heights):
            while stack and x <  stack[-1][2]:
                ans  = max(ans,(i-stack[-1][0]-1) * stack[-1][2])
                stack.pop()
            if stack:
                stack.append((stack[-1][1],i,x))
            else:
                stack.append((-1,i,x))
            
        if stack:
            right_end = stack[-1][1]
            for tup in stack:
                ans = max(ans,(right_end-tup[0])*tup[2])

        
        return ans

