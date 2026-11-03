class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        total = m*n
        ans = []
        count = 0
        i = 0
        j = 0
        rb = n-1
        db = m-1
        lb = 0
        ub = 1
        cur = 'r'
        while True:
            if cur == 'r' and j <= rb:
                ans.append(matrix[i][j])
                if j == rb:
                    cur = 'd'
                    i += 1
                    rb -= 1
                else:
                    j += 1
            elif cur == 'd' and i <= db:
                ans.append(matrix[i][j])
                if i == db:
                    cur = 'l'
                    j -= 1
                    db -= 1
                else:
                    i += 1
            
            elif cur == 'l' and j >= lb:
                ans.append(matrix[i][j])
                if j == lb:
                    cur = 'u'
                    i -= 1
                    lb += 1
                else:
                    j -= 1
            elif cur == 'u' and i >= ub:
                ans.append(matrix[i][j])
                
                if i == ub:
                    cur = 'r'
                    j += 1
                    ub += 1
                else:
                    i -= 1
            
            count += 1
            if count == total:
                break
        
        return ans