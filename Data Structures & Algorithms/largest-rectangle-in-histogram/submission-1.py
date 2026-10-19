class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0

        stack = []

        for i,x in enumerate(heights+[0]):

            while stack and x < heights[stack[-1]]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i-left -1
                ans = max(ans, height*width)
            stack.append(i) 
        
        return ans

