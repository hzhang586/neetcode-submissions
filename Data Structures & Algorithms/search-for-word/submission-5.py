class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        m = len(board)
        n = len(board[0])
        l = len(word)

        def dfs(r,c,i):

            if i == l:
                return True
            if not (r >= 0 and r < m and c >= 0 and c < n):
                return False
            if (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if dfs(nr,nc,i+1):
                    return True
            visited.remove((r,c))
            return False

        
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        
        return False


