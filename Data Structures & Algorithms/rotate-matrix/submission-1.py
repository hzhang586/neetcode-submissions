class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        mid = n//2 

        for i in range(mid):
            for j in range(i,n-i-1):
                tmp1 = matrix[i][j]
                tmp2 = matrix[j][n-i-1]
                tmp3 = matrix[n-i-1][n-j-1]
                tmp4 = matrix[n-j-1][i]

                matrix[j][n-i-1] = tmp1
                matrix[n-i-1][n-j-1] = tmp2
                matrix[n-j-1][i] = tmp3
                matrix[i][j] = tmp4
        