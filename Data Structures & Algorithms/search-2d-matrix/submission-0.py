class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        r_left,r_right = -1, len(matrix)
        while r_left + 1 < r_right:

            r_mid = (r_left+r_right) // 2
            if matrix[r_mid][0] == target:
                return True
            
            if matrix[r_mid][0] < target:
                r_left = r_mid
            else:
                r_right = r_mid
        
        if r_left == -1:
            return False
        
        c_left, c_right = -1,len(matrix[0])

        while c_left+1 < c_right:
            c_mid = (c_left+c_right) // 2
            if matrix[r_left][c_mid] == target:
                return True
            
            if matrix[r_left][c_mid] < target:
                c_left = c_mid
            else:
                c_right = c_mid
        
        return False
            

        