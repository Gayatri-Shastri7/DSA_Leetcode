class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        find = find_empty(board)
        if not find:
            return True
        else:
            (row,col) = find
        
        for i in range(1,10):
            if valid(board, str(i), (row,col)):
                board[row][col] = str(i)
            
                if self.solveSudoku(board):
                    return True

                board[row][col] = '.'
        
        return False
        
def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    box_x = pos[0]//3
    box_y = pos[1]//3
    
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True
        
def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == '.':
                return row,col
    return None