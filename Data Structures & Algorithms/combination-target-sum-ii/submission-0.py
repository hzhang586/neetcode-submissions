class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []
        n = len(candidates)
        candidates.sort()

        def dfs(i,target):

            if target == 0:
                ans.append(path.copy())
                return
            
            if i == n or target < 0:
                return 
            
            path.append(candidates[i])
            dfs(i+1,target-candidates[i])
            path.pop()

            j = i+1

            while j < n and candidates[j] == candidates[i]:
                j += 1
            
            dfs(j,target)
        
        dfs(0,target)

        return ans

        