class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        used = set()
        n = len(nums)
        def dfs():

            if len(path) == n:
                ans.append(path.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                
                path.append(num)
                used.add(num)
                dfs()
                path.pop()
                used.remove(num)
        dfs()
        return ans

        