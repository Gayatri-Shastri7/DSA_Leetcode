# https://www.youtube.com/watch?v=ZYpYur0znng&ab_channel=takeUforward
'''
Method1: 
Traverse each row and then check

METHOD2:
Sort each row and then do binary search

Method3 : Most Optimised

1.Place ptr at last coloumn of the 1st row
check the given element is less than or gr than the at element then move down, right, left, top accdingly 


'''
 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1                
            else:
                return True

        return False
        