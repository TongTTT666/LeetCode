class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        # 第一维升序第二维降序
        for i in range(len(envelopes)):
            envelopes[i][1] *= -1
        envelopes.sort()
        for i in range(len(envelopes)):
            envelopes[i][1] *= -1
        
        # 再用300题的技巧，二分查找
        tails = [0 for i in range(len(envelopes))]
        size = 0
        
        for x in envelopes:
            i, j = 0, size
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < x[1]:
                    i = mid + 1
                else:
                    j = mid
            # 更新tails，已找到x[1]在tails中的排序 i=j
            tails[i] = x[1]
            if i == size:
                size += 1
                
                
        return size