class Solution:
#Not linear time and using additional memory
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0 
                    
          
-----------------------------
#Constant space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col = False       
        
        for i in range(0,len(matrix)):
            if matrix[i][0] == 0:
                col = True
            for j in range(0,len(matrix[0])):
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(0,len(matrix[0])):
                matrix[0][j] = 0
      
        if col:
            for i in range(0,len(matrix)):
                matrix[i][0] = 0
            
