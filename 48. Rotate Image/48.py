class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 将矩阵顺时针旋转90度 可以分解为 转置+列镜像两步
        
        
        # 转置
        def T(matrix):
            i = j = 0
            n = len(matrix)
            
            for i in range(n):
                j = 0
                while j < i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    j += 1
                
        # 按列镜像
        def I(matrix):
            for j in range(len(matrix)//2):
                for i in range(len(matrix)):
                    matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]
        
        T(matrix)
        I(matrix)

