class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        box_map = {}
        for i in range(9):
            row_map[i] = set()
        for j in range(9):
            col_map[j] = set()
        
        for i in range(3):
            for j in range(3):
                box_map[(i,j)] = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_r = i//3
                box_c = j//3
                if num != ".":
                    if   num not in row_map[i] and num not in col_map[j] and num not in box_map[(box_r,box_c)]:
                        row_map[i].add(num)
                        col_map[j].add(num)
                        box_map[(box_r,box_c)].add(num)
                    else:
                        return False
        
        return True
            



        