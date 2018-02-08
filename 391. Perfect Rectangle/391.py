class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 类似于贪心问题
        # 规则比较多，首先所有小矩形的面积加起来必须等于大矩形
        # 其次，每个内部顶点只能出现两次或者四次，一旦不是2次或4次
        # 就是有问题，要么重复，要么就是有空档
    
        # 首先要弄一个字典，专门记录每一个点出现的次数
        record_vertex = {}
        # 接着要想办法记录最大的两个顶点坐标
        # 这里先初始化一下 (X1, Y1) (X2, Y2)
        X1, Y1, X2, Y2 = float('inf'), float('inf'), -float('inf'), -float('inf')
        # 初始化总面积
        area = 0
        
        for vertex in rectangles:
            # 提取坐标 (x1, y1) (x2, y2)
            x1, y1, x2, y2 = vertex[0], vertex[1], vertex[2], vertex[3]
            # 最大边缘坐标统计
            X1, Y1, X2, Y2 = min(x1, X1), min(y1, Y1), max(x2, X2), max(y2, Y2)
            # 根据这两个点的坐标求出四个坐标，并对其次数加1，位置[bl, br, tl, tr]
            points = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            # 可以算面积了，把面积加一加
            area += (x2-x1) * (y2-y1)
            # 安排字典当中相应key所对应的value值加1
            for p in points: 
                if p not in record_vertex:
                    record_vertex[p] = 1
                else:
                    record_vertex[p] += 1
                    
        # 面积是否相等？
        if area != (Y2-Y1) * (X2-X1):
            return False
        
        # 确定边界点
        VERTEX = [(X1, Y1), (X2, Y1), (X1, Y2), (X2, Y2)]
        
        # 边界点是必须出现的，没出现肯定就有空
        for p in VERTEX:
            if p not in record_vertex:
                return False
        
        # 每个内部顶点是否只出现了2次或者4次，并且还不能是边缘大顶点
        for p in record_vertex:
            if p not in VERTEX and record_vertex[p] % 2 == 1:
                return False
        
        return True