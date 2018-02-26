class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 创建一个记录的集合
        nums = set()
        _sum = tmp = 0
        while True:
            
            if n not in nums:
                nums.add(n)
            else:
                return False
            
            while n > 0:
                tmp = n % 10
                _sum += tmp * tmp 
                n //= 10
                
            if _sum == 1:
                return True
            else:
                n = _sum
                _sum = 0

               
        
       