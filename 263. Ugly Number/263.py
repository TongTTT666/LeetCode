class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 例外情况 1
        if num == 1:
            return True
        if num <= 0:
            return False
        
        # 一关一关的来 先5再3再2
        # 一关一关过就需要用到if elseif
        while num > 1:
            if num % 5 == 0:
                num //= 5
            elif num % 3 == 0:
                num //= 3
            elif num % 2 == 0:
                num //= 2
            else:
                return False
                
        return True
        
        