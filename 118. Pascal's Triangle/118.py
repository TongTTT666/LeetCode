class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 初始化
        if numRows == 0:
            return []
        
        tr = [[1]]
        # 注意这句代码的书写方式
        for i in range(numRows-1):
            tr.append([x + y for x, y in zip([0] + tr[i], tr[i] + [0])])
            
        return tr