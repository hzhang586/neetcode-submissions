class Solution:
    def trap(self, height: List[int]) -> int:

        prefix_max = height[0]
        prefix_max_l = [0]*len(height)
        for i in range(1,len(height)):
            if height[i-1] > prefix_max:
                prefix_max = height[i-1]
            prefix_max_l[i] = prefix_max

        suffix_max = height[-1]
        suffix_max_l = [0]*len(height)
        for j in range(len(height)-1,1,-1):
            if height[j] > suffix_max:
                suffix_max = height[j]
            
            suffix_max_l[j-1] = suffix_max
        

        ans = 0
        for i,x in enumerate(height):
            ans += max(0,min(prefix_max_l[i],suffix_max_l[i])-x)
        return ans


        