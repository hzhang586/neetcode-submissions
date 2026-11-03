class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
        zr_first = False
        zc_first = False

        if matrix[0][0] == 0:
            zr_first = True
            zc_first = True
        else:
            for i in range(1,m):
                if matrix[i][0] == 0:
                    zc_first = True
                    break
            for j in range(1,n):
                if matrix[0][j] == 0:
                    zr_first = True
                    break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        if zr_first:
            for j in range(n):
                matrix[0][j] = 0
        if zc_first:
            for i in range(m):
                matrix[i][0] = 0
        
        