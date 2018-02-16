class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 0
        # 作短除法算二进制，直接求短除法中出现的余数1的数目
        while n > 0:
            if n % 2 == 1:
                t += 1    
            n //= 2
            
        return t