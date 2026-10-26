class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        path = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(i):

            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(n):
                if (j in cols or i-j in diag1 or i+j in diag2):
                    continue
                path.append(j)
                cols.add(j)
                diag1.add(i-j)
                diag2.add(i+j)
                dfs(i+1)
                path.pop()
                cols.remove(j)
                diag1.remove(i-j)
                diag2.remove(i+j)           
            
              
        dfs(0)
        result = []
        for l in ans:
            r = []
            for v in l:
                s = ""
                for i in range(n):
                    if i == v:
                        s += 'Q'
                    else:
                        s += '.'
                r.append(s)
            result.append(r)
        return result
        