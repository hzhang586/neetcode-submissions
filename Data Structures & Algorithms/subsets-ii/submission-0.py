class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)
        nums.sort()

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            j = i+1
            while j < n and nums[j] == nums[i]:
                j += 1
            
            dfs(j)
            
            
            
        
        dfs(0)

        return ans
        