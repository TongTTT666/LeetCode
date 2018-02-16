class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # 求亮点之间的距离
        def getDistance(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
            
            
        p = [p1, p2, p3, p4]
        dic = collections.Counter()   # 定义计数器字典，作为初始化
        
        for i in range(1, len(p)):
            for j in range(i):
                dic[getDistance(p[i], p[j])] += 1
        
        
        return 2 in dic.values() and 4 in dic.values()
        