class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        head = 0
        res = ""
        # 正常情况先做，后面再弄非正常情况
        while head + 2*k - 1 < len(s):
                tmp = s[head:head+k]
                res += tmp[::-1]
                head += k
                res += s[head:head+k]
                head += k
        
        
        # 正常情况与两种特殊情况
        if head == len(s):
            return res
        elif head + k - 1 >= len(s):
            tmp = s[head:]
            return res + tmp[::-1]
        elif head + 2*k - 1 >= len(s):
            tmp = s[head:head+k]
            return res + tmp[::-1] + s[head+k:]
       
    
            
        