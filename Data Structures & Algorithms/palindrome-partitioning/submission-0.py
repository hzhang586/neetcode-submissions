class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        path = []
        ans  = []
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(i+1,n+1):
                if s[i:j] == s[i:j][::-1]:
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()
                
                
                
        
        dfs(0)
        return ans
        