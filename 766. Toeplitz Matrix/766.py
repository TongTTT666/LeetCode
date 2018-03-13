class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp = matrix[i][j]
                r, c = i, j
                while r < len(matrix) and c < len(matrix[0]):
                    if matrix[r][c] == tmp:
                        r += 1
                        c += 1
                    else:
                        return False
                
        return True