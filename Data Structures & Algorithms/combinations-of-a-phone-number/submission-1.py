class Solution:

    numMap = {'2':"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8": "tuv","9":"wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:

        ans = []
        path = []
        n = len(digits)
        if not digits:
            return []
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
        
            for c in self.numMap[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
        
        dfs(0)
    
        return ans

        