class Solution:
    def kthSmallest(self, matrix, k):
        # 对range进行二分，而不是对index
        # 也即，给定一个range，计算mid缩小这个range，使其最终逼近一个数
        # 先定范围，就是矩阵中的最大数和最小数\
        row, col = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[row-1][col-1]
        
        while left < right:
            mid = left + (right - left) // 2
            # 目标就是寻找小于等于mid的数究竟有几个
            # count 用来计数
            count = 0      
            for i in range(row):
                j = 0
                while j <= col-1 and matrix[i][j] <= mid:
                    j += 1
                count += j
            # 判断有多少个数比mid小或者等于，然后调整left和right
            if count < k:
                left = mid + 1
            else:
                right = mid
                
        return left
        