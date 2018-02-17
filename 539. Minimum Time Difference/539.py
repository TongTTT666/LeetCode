# 法1：逐一比较，耗时很多超时了
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        mindif = float('inf')
        # 用O(n^2)时间
        for i in range(len(timePoints)):
            for j in range(i):
                # 分别提取两个时间
                t0 = timePoints[i]
                t1 = timePoints[j]
                # 分隔开
                t0 = t0.split(":")
                t1 = t1.split(":")

                # 全部换算为分钟用T0 T1表示
                T0 = int(t0[0])*60 + int(t0[1])
                T1 = int(t1[0])*60 + int(t1[1]) 
                
                temp = min(abs(T1-T0), 1440-abs(T1-T0))
                if temp < mindif:
                    mindif = temp
                

            # 计算，时间不能大于720 也即1440的一半
        return mindif
        

# 法2：想办法省时间，如果temp = 0，则不用再算，这个就通过了
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        mindif = float('inf')
        # 用O(n^2)时间
        for i in range(len(timePoints)):
            for j in range(i):
                # 分别提取两个时间
                t0 = timePoints[i]
                t1 = timePoints[j]
                # 分隔开
                t0 = t0.split(":")
                t1 = t1.split(":")

                # 全部换算为分钟用T0 T1表示
                T0 = int(t0[0])*60 + int(t0[1])
                T1 = int(t1[0])*60 + int(t1[1]) 
                
                temp = min(abs(T1-T0), 1440-abs(T1-T0))
                if temp < mindif:
                    mindif = temp
                if temp == 0:
                    return 0
                

            # 计算，时间不能大于720 也即1440的一半
        return mindif
        
# 法3：试着用排序，两两相减
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440:
            return 0
        
        mindif = float('inf')
        # 用排序去做，首先要转化为分钟
        def convert(time):
            return int(time[:2])*60 + int(time[3:])
        
        timePoints = map(convert, timePoints)
        timePoints = sorted(timePoints)
        
        
        return min((t1 - t0) % 1440 for t0, t1 in zip(timePoints, timePoints[1:] + timePoints[:1]))