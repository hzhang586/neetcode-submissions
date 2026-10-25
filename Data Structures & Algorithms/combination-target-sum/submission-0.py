class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        comb = []
        n = len(nums)
        def dfs(i,target):
            
            if target == 0:
                ans.append(comb.copy())
                return
            if i >= n or target < 0:
                return
            
            comb.append(nums[i])
            dfs(i,target-nums[i])
            comb.pop()
            dfs(i+1,target)

        dfs(0,target)
        return ans            
